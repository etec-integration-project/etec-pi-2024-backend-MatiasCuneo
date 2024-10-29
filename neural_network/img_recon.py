import tensorflow as tf

model = tf.keras.models.load_model('mnist_model.h5')

def predict_digit(image):
    image = (255 - image.reshape((1, 28, 28, 1)).astype('float32')) / 255
    print(image)
    predictions = model.predict(image)
    return predictions.argmax()

