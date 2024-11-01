from flask import request, jsonify
import tensorflow as tf
from sqlalchemy import func
from config import app, db
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('mnist_model.h5')

def predict_digit(image):
    image = (255 - np.array(image).reshape((1, 28, 28, 1)).astype('float32')) / 255
    predictions = model.predict(image)
    return int(predictions.argmax())

@app.route("/tf/", methods=["GET"])
def getOnActive():
  sql = db.session.query(func.current_timestamp()).scalar()
  return str(sql)

@app.route('/tf/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        image = Image.open(file).convert('L')
        image = image.resize((28, 28))
        image_array = np.array(image)

        try:
            result = predict_digit(image_array)
            return jsonify({"success": result}), 200
        except:
            return jsonify({"error": "Failed to get prediction" }), 500

    return jsonify({"error": "Something went wrong"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=8501)