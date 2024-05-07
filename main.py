from sqlalchemy import func
from config import app, db

@app.route("/", methods=["GET"])
def getOnActive():
  sql = db.session.query(func.current_timestamp()).scalar()
  return str(sql)

if __name__ == "__main__":
  with app.app_context():
    db.create_all()

  app.run(debug=True, port=5000, host='0.0.0.0')