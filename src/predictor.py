import os
import numpy as np
import tensorflow as tf
from keras.utils import load_img, img_to_array


class Predictor:
    def __init__(self, tf_model, class_names, image_path):
        self.tf_model = tf_model
        self.class_names = class_names
        self.image_path = image_path
    
    def predict(self):
        img = load_img(self.image_path, target_size=(150, 150))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        prediction = self.tf_model.predict(images, batch_size=10)
        
        result = self.class_names[np.argmax(prediction)]
        return result