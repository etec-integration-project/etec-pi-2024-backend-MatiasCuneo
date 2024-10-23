import tensorflow as tf
import keras

model = tf.keras.models.load_model('mnist_model.h5')

def predict_digit(image):
    image = (255 - image.reshape((1, 28, 28, 1)).astype('float32')) / 255
    predictions = model.predict(image)
    return predictions.argmax()

