from flask import request, jsonify
import tensorflow as tf
from sqlalchemy import func
from config import app, db
from PIL import Image
import numpy as np
import tempfile

model = tf.keras.models.load_model('mnist_model.h5')

def predict_digit(image):
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

    if file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            temp_path = tmp.name
            file.save(temp_path)
            print(f"Saved temporary image at {temp_path}")

            image = Image.open(temp_path).convert('L')
            image = image.resize((28, 28))
            image = (255 - np.array(image).reshape((1, 28, 28, 1)).astype('float32')) / 255

        try:
            result = predict_digit(image)
            return jsonify({"success": result}), 200
        except:
            return jsonify({"error": "Failed to get prediction" }), 500

    return jsonify({"error": "Something went wrong"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=8501)