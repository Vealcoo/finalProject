from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from keras.models import Sequential
import sys
import os
from os import listdir, walk
from os.path import isfile, isdir, join
from glob import glob
import numpy as np
from keras.layers import Convolution2D, Dense, Input, Flatten, Dropout, MaxPooling2D, BatchNormalization, GlobalAveragePooling2D, Concatenate

def f1(y_true, y_pred):


    ### macro version
    tp = K.sum(K.cast(y_true*y_pred, 'float'), axis=0)
    tn = K.sum(K.cast((1-y_true)*(1-y_pred), 'float'), axis=0)
    fp = K.sum(K.cast((1-y_true)*y_pred, 'float'), axis=0)
    fn = K.sum(K.cast(y_true*(1-y_pred), 'float'), axis=0)

    p = K.mean(tp / (tp + fp + K.epsilon()))
    r = K.mean(tp / (tp + fn + K.epsilon()))

    f1 = 2*p*r / (p+r+K.epsilon())
    #f1 = tf.where(tf.is_nan(f1), tf.zeros_like(f1), f1)
    return f1

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# cls_list = ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'UNK', 'VASC']


path = '/home/marc/Binary_Training/resnetFeature'
files = listdir(path)

# load model
# model = load_model('CV1_DF_weight_best.hdf5') #---cant get custom metric in training---

model_AK = load_model("/home/marc/Binary_Training/AK_Binary/CV4_AK_weight_best.hdf5",
                        custom_objects={'f1':f1})

model_BCC = load_model("/home/marc/Binary_Training/BCC_Binary/CV1_BCC_weight_best.hdf5",
                        custom_objects={'f1':f1})

model_BKL = load_model("/home/marc/Binary_Training/BKL_Binary/CV1_BKL_weight_best.hdf5",
                        custom_objects={'f1':f1})

model_DF = load_model("/home/marc/Binary_Training/DF_Binary/CV3_DF_weight_best.hdf5",
                        custom_objects={'f1':f1})

model_MEL = load_model("/home/marc/Binary_Training/MEL_Binary/CV1_MEL_weight_best.hdf5",
                        custom_objects={'f1':f1})

model_NV = load_model("/home/marc/Binary_Training/NV_Binary/CV1_NV_weight_best.hdf5",
                        custom_objects={'f1':f1})

model_SCC = load_model("/home/marc/Binary_Training/SCC_Binary/CV4_SCC_weight_best.hdf5",
                        custom_objects={'f1':f1})

model_VASC = load_model("/home/marc/Binary_Training/VASC_Binary/CV3_VASC_weight_best.hdf5",
                        custom_objects={'f1':f1})

output = "ensembleFeature"
if not os.path.exists(output):
       os.makedirs(output)

for f in files:
    fullpath = join(path, f)
    outputName = f.split(os.sep)[-1].split(".")[0]
    x = np.load(fullpath)
    x = np.expand_dims(x, axis = 0)
#     x = preprocess_input(x)
    
    feature_AK = model_AK.predict(x)
#     feature_AK = np.reshape(feature_AK, feature_AK.shape[1:])
   
    feature_BCC = model_BCC.predict(x)
#     feature_BCC = np.reshape(feature_BCC, feature_BCC.shape[1:])
    
    feature_BKL = model_BKL.predict(x)
#     feature_BKL = np.reshape(feature_BKL, feature_BKL.shape[1:])
    
    feature_DF = model_DF.predict(x)
#     feature_DF = np.reshape(feature_DF, feature_DF.shape[1:])
    
    feature_MEL = model_MEL.predict(x)
#     feature_MEL = np.reshape(feature_MEL, feature_MEL.shape[1:])
    
    feature_NV = model_NV.predict(x)
#     feature_NV = np.reshape(feature_NV, feature_NV.shape[1:])
    
    feature_SCC = model_SCC.predict(x)
#     feature_SCC = np.reshape(feature_SCC, feature_SCC.shape[1:])
    
    feature_VASC = model_VASC.predict(x)
#     feature_VASC = np.reshape(feature_VASC, feature_VASC.shape[1:])
    
    feature_output = np.vstack((feature_AK,feature_BCC,feature_BKL,feature_DF,feature_MEL,feature_NV,feature_SCC,feature_VASC))
    
    print feature_output
#     feature_output = np.array(list(feature_output))
    
#     feature_output = np.reshape(feature_outputls, 16)
    
    feature_output = feature_output.flatten()
 
    np.save(output+"/"+ outputName, feature_output)
    

    
