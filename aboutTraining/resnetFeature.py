from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from keras.applications.resnet50 import ResNet50

from keras.models import Sequential
import sys
import os
from os import listdir, walk
from os.path import isfile, isdir, join
from glob import glob
import numpy as np
from keras.layers import Convolution2D, Dense, Input, Flatten, Dropout, MaxPooling2D, BatchNormalization, GlobalAveragePooling2D, Concatenate

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

model = ResNet50(weights='imagenet',
                include_top=False,
                input_shape=(224, 224, 3))
model.summary()


#########################################################
path = 'ISIC_2019_Training_Input/'
files = listdir(path)

os.makedirs("resnetFeature/")
for f in files:
    fullpath = join(path, f)
    outputName = f.split(os.sep)[-1].split(".")[0]
    img = image.load_img(fullpath, target_size=(224, 224))
    if img is None:
        continue
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    feature = model.predict(x)
    feature = np.reshape(feature, feature.shape[1:])
    np.save("resnetFeature/"+outputName, feature)
print'OK'
##########################################################    

