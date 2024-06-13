import numpy as np
import os
import random
import pandas as pd
from PIL import Image


# ========== PREPROCESADO DE IMAGENES ==========
def load_dataset(dataset, path):
    data = pd.read_csv(os.path.join(path, dataset) + '.csv')

    y = data['label'].values
    X = data.drop('label', axis=1).values

    return np.array(X), np.array(y).astype('uint8')

def rotate_images(images, angle):
    for image in images:
        img = Image.fromarray(image.reshape(28, 28))
        rotated_img = img.rotate(random.randint(-(angle), angle))
        image = np.array(rotated_img)
        image.flatten()
    return images

def translate_images(images):
    shift = (random.randint(-5, 5), random.randint(-5, 5))
    for image in images:
        img = Image.fromarray(image.reshape(28, 28))
        image = img.transform(img.size, Image.AFFINE, (1, 0, shift[0], 0, 1, shift[1]))
    return images

def preprocessing(images):
    return translate_images(rotate_images(images, 9))

X, y = load_dataset('train', '../mnist_dataset')

keys = np.array(range(X.shape[0]))
np.random.shuffle(keys)

X = X[keys]
y = y[keys]

X = X.reshape(X.shape[0], -1).astype(np.float32)

preprocessing(X)

X = (X - 127.5) / 127.5

# ========== TESTING ==========
print(X[0])
