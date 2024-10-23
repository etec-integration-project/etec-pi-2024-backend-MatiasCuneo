from flask import request, jsonify
from sqlalchemy import func
from config import app, db
from etec-pi-2024-backend-MatiasCuneo.neural_network.img_recon import
predict_digit

@app.route("/", methods=["GET"])
def getOnActive():
  sql = db.session.query(func.current_timestamp()).scalar()
  return str(sql)

@app.route("/prediction", methods=["GET"])
def getPrediction():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        prediction = predict_digit(imagen)
        return jsonify({ "success": prediction }), 200

    return jsonify({ "error": "Something went wrong" }), 500

if __name__ == "__main__":
  with app.app_context():
    db.create_all()

  app.run(debug=True, port=5000, host='0.0.0.0')
