import numpy as np
import os
import pandas as pd
from PIL import Image

def load_dataset(dataset, path):
    data = pd.read_csv(os.path.join(path, dataset) + '.csv')

    y = data['label'].values
    X = data.drop('label', axis=1).values

    return np.array(X), np.array(y).astype('uint8')

X, y = load_dataset('train', '../mnist_dataset')

print(X[0])
