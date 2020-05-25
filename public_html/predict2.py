# coding:utf-8
import os
import PIL.Image
import csv
import numpy as np
import sys
from sklearn.model_selection import StratifiedKFold

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing import image
from keras import applications
from keras.models import Sequential
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input
from keras.applications.inception_v3 import InceptionV3
from keras.applications.resnet50 import preprocess_input
from keras.applications.resnet50 import ResNet50
import time


import MySQLdb


def f1(y_true, y_pred):
    # macro version
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


if __name__ == '__main__':
    
#     def f1(y_true, y_pred):
#         # macro version
#         tp = K.sum(K.cast(y_true*y_pred, 'float'), axis=0)
#         tn = K.sum(K.cast((1-y_true)*(1-y_pred), 'float'), axis=0)
#         fp = K.sum(K.cast((1-y_true)*y_pred, 'float'), axis=0)
#         fn = K.sum(K.cast(y_true*(1-y_pred), 'float'), axis=0)

#         p = K.mean(tp / (tp + fp + K.epsilon()))
#         r = K.mean(tp / (tp + fn + K.epsilon()))

#         f1 = 2*p*r / (p+r+K.epsilon())
#         #f1 = tf.where(tf.is_nan(f1), tf.zeros_like(f1), f1)
#         return f1

# with con:

#     cur = con.cursor()

#     cur.execute("SELECT path FROM img_path WHERE NO='3'")

#     path = cur.fetchall()

    path = "upload/1576350517_500px-Melanoma.jpg"
    DP_Num = 1
#     path = 'blue.jpeg'
    

resnet50_feature = applications.ResNet50(weights='imagenet',
                                            include_top=False,
                                            input_shape=(224, 224, 3))

inceptionV3_feature = applications.InceptionV3(weights='imagenet',
                                            include_top=False,
                                            input_shape=(299, 299, 3))

rimg = image.load_img(path, target_size=(224, 224, 3))
rimg_data = image.img_to_array(rimg)
rimg_data = np.expand_dims(rimg_data, axis=0)
rimg_data = preprocess_input(rimg_data)

rfeature = resnet50_feature.predict(rimg_data)
rfeature = np.reshape(rfeature, rfeature.shape[1:])

iimg = image.load_img(path, target_size=(299, 299, 3))
iimg_data = image.img_to_array(iimg)
iimg_data = np.expand_dims(iimg_data, axis=0)
iimg_data = preprocess_input(iimg_data)

ifeature = inceptionV3_feature.predict(iimg_data)
ifeature = np.reshape(ifeature, ifeature.shape[1:])



# resnet50 ensemble


r_model_AK = load_model("finalModel/resnet50/CV4_AK_weight_best.hdf5",
                        custom_objects={'f1': f1})

r_model_BCC = load_model("finalModel/resnet50/CV1_BCC_weight_best.hdf5",
                         custom_objects={'f1': f1})

r_model_BKL = load_model("finalModel/resnet50/CV1_BKL_weight_best.hdf5",
                         custom_objects={'f1': f1})

r_model_DF = load_model("finalModel/resnet50/CV3_DF_weight_best.hdf5",
                        custom_objects={'f1': f1})

r_model_MEL = load_model("finalModel/resnet50/CV1_MEL_weight_best.hdf5",
                         custom_objects={'f1': f1})

r_model_NV = load_model("finalModel/resnet50/CV1_NV_weight_best.hdf5",
                        custom_objects={'f1': f1})

r_model_SCC = load_model("finalModel/resnet50/CV4_SCC_weight_best.hdf5",
                         custom_objects={'f1': f1})

r_model_VASC = load_model("finalModel/resnet50/CV3_VASC_weight_best.hdf5",
                          custom_objects={'f1': f1})

x = np.expand_dims(rfeature, axis=0)

rfeature_AK = r_model_AK.predict(x)

rfeature_BCC = r_model_BCC.predict(x)

rfeature_BKL = r_model_BKL.predict(x)

rfeature_DF = r_model_DF.predict(x)

rfeature_MEL = r_model_MEL.predict(x)

rfeature_NV = r_model_NV.predict(x)

rfeature_SCC = r_model_SCC.predict(x)

rfeature_VASC = r_model_VASC.predict(x)


resnet50_feature = np.vstack((rfeature_AK, rfeature_BCC, rfeature_BKL,rfeature_DF, rfeature_MEL, rfeature_NV, rfeature_SCC, rfeature_VASC))

resnet50_feature = resnet50_feature.flatten()


# resnet50_feature = resnet50_model.predict(rfeature_output)

# inceptionV3 ensemble


i_model_AK = load_model("finalModel/inceptionV3/AK_weights.best.hdf5.CV1",
                        custom_objects={'f1': f1})

i_model_BCC = load_model("finalModel/inceptionV3/BCC_weights.best.hdf5.CV3",
                         custom_objects={'f1': f1})

i_model_BKL = load_model("finalModel/inceptionV3/BKL_weights.best.hdf5.CV5",
                         custom_objects={'f1': f1})

i_model_DF = load_model("finalModel/inceptionV3/DF_weights.best.hdf5.CV2",
                        custom_objects={'f1': f1})

i_model_MEL = load_model("finalModel/inceptionV3/MEL_weights.best.hdf5.CV3",
                         custom_objects={'f1': f1})

i_model_NV = load_model("finalModel/inceptionV3/NV_weights.best.hdf5.CV3",
                        custom_objects={'f1': f1})

i_model_SCC = load_model("finalModel/inceptionV3/SCC_weights.best.hdf5.CV5",
                         custom_objects={'f1': f1})

i_model_VASC = load_model("finalModel/inceptionV3/VASC_weights.best.hdf5.CV3",
                          custom_objects={'f1': f1})

y = np.expand_dims(ifeature, axis=0)

ifeature_AK = i_model_AK.predict(y)

ifeature_BCC = i_model_BCC.predict(y)

ifeature_BKL = i_model_BKL.predict(y)

ifeature_DF = i_model_DF.predict(y)

ifeature_MEL = i_model_MEL.predict(y)

ifeature_NV = i_model_NV.predict(y)

ifeature_SCC = i_model_SCC.predict(y)

ifeature_VASC = i_model_VASC.predict(y)


inceptionV3_feature = np.vstack((ifeature_AK, ifeature_BCC, ifeature_BKL,ifeature_DF, ifeature_MEL, ifeature_NV, ifeature_SCC, ifeature_VASC))

inceptionV3_feature = inceptionV3_feature.flatten()


# inceptionV3_feature = inceptionV3_model.predict(ifeature_output)

# finalEnsemble


resnet50_feature = np.expand_dims(resnet50_feature, axis=0)
print resnet50_feature
resnet50Ensmeble = load_model("finalModel/resnet50Best.hdf5",
                              custom_objects={'f1': f1})
finalr = resnet50Ensmeble.predict(resnet50_feature)

inceptionV3_feature = np.expand_dims(inceptionV3_feature, axis=0)
print inceptionV3_feature
inceptionV3Ensmeble = load_model("finalModel/inceptionV3Best.hdf5",
                                 custom_objects={'f1': f1})
finali = inceptionV3Ensmeble.predict(inceptionV3_feature)

finalFeature = np.vstack((finalr, finali))
print finalFeature.shape
finalFeature = finalFeature.flatten()
print finalFeature.shape

finalModel = load_model("finalModel/iAndR_allBest.hdf5",
                        custom_objects={'f1': f1})


output = finalModel.predict(finalFeature)
print output

con = MySQLdb.Connect(host='localhost',
                     port=3306,
                     user='skindb',
                     passwd='gEqM9v9kndcVGjXf',
                     db='SKINDB',
                     charset='utf8')
#DP_Num
sql_insert = ("INSERT INTO history(`DP_Num`,`AK`,`BCC`,`BKL`,`DF`,`MEL`,`NV`,`SCC`,`VASC`)"  "VALUES(DP_Num,%s,%s,%s,%s,%s,%s,%s,%s)")
sql_data = (output[0], output[1], output[2], output[3],
           output[4], output[5], output[6], output[7])
con.execute(sql_insert, sql_data)
con.commit()
con.close()

