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
def getConfigByUserId(user_id):
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

@app.route("/create_config/<string:user_id>", methods=["POST"])
def createConfigByUserId(user_id):
  try:
    uuid_object = UUID(user_id, version=4)
  except ValueError:
    return jsonify({ "error": "ID is not a valid UUID" }), 400

  data = request.get_json()

  layersNum = data.get("layersNum")
  neuronsNum = data.get("neuronsNum")
  optimizer = data.get("optimizer")
  lossFunc = data.get("lossFunc")
  alpha = data.get("alpha")
  weightsId = data.get("weightsId")

  config = UserConfig(
    userId=user_id,
    layersNum=layersNum,
    neuronsNum=neuronsNum,
    optimizer=optimizer,
    lossFunc=lossFunc,
    alpha=alpha,
    weightsId=weightsId
  )

  try:
    db.session.add(config)
    db.session.commit()
  except DataError as e:
    return jsonify({ "error": e }), 500
  
  return jsonify({ "success": "User Config added successfully!" }), 200

#Just for development purposes
@app.route("/configs", methods=["GET"])
def getAllConfigs():
  try:
    configs = UserConfig.query.all()
    configs_json = list(map(lambda x: x.to_json(), configs))
  except DataError as e:
    return jsonify({ "error": e }), 500
  
  return jsonify({ "success": configs_json }), 200

@app.route("/update_config/<string:id>", methods=["PATCH"])
def updateConfigById(id):
  try:
    uuid_object = UUID(id, version=4)
  except ValueError:
    return jsonify({ "error": "ID is not a valid UUID" }), 400
  
  try:
    config = UserConfig.query.filter_by(id=id).first()
    if not config: return jsonify({ "error": "No Config found" }), 404
  except DataError as e_1:
    return jsonify({ "error": e }), 500
  
  data = request.json
  config.layersNum = data.get("layersNum", config.layersNum)
  config.neuronsNum = data.get("neuronsNum", config.neuronsNum)
  config.optimizer = data.get("optimizer", config.optimizer)
  config.lossFunc = data.get("lossFunc", config.lossFunc)
  config.alpha = data.get("alpha", config.alpha)

  try:
    db.session.commit()
  except DataError as e_2:
    return jsonify({ "error": e_2 }), 500
  
  return jsonify({ "success": "Config updated successfully!" }), 200
  
if __name__ == "__main__":
  with app.app_context():
    db.create_all()

  app.run(debug=True, port=5000, host='0.0.0.0')