from flask import request, jsonify
from sqlalchemy import func
from sqlalchemy.exc import DataError
from config import app, db
from models import UserConfig, Weights
from uuid import UUID

@app.route("/", methods=["GET"])
def getOnActive():
  sql = db.session.query(func.current_timestamp()).scalar()
  return str(sql)

@app.route("/usrconfig/<string:user_id>", methods=["GET"])
def getConfigById(user_id):
  try:
    uuid_object = UUID(user_id, version=4)
  except ValueError:
    return jsonify({ "error": "ID is not a valid UUID" }), 400
  
  try:
    userConfig = UserConfig.query.filter_by(userId=user_id).first()
    if not userConfig: return jsonify({ "error": "No Config Found!" }), 404
  except DataError as e:
    return jsonify({ "error": e }), 500

  return jsonify({ "success": userConfig.to_json() }), 200

if __name__ == "__main__":
  with app.app_context():
    db.create_all()

  app.run(debug=True, port=5000, host='0.0.0.0')