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

#os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# cls_list = ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'UNK', 'VASC']


os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

if __name__ == '__main__':
	start_time = time.time()   
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

#    path = sys.argv[1]

path = 'upload/1576335996_Screen Shot 2019-12-04 at 8.56.05 PM.png'
    

rimg = image.load_img(path, target_size=(224, 224, 3))
rimg_data = image.img_to_array(rimg)
rimg_data = np.expand_dims(rimg_data, axis=0)
rimg_data = preprocess_input(rimg_data)

resnet50_feature = applications.ResNet50(weights='imagenet',
                                            include_top=False,
                                            input_shape=(224, 224, 3))

rfeature = resnet50_feature.predict(rimg_data)
K.clear_session()
rfeature = np.reshape(rfeature, rfeature.shape[1:])

iimg = image.load_img(path, target_size=(299, 299, 3))
iimg_data = image.img_to_array(iimg)
iimg_data = np.expand_dims(iimg_data, axis=0)
iimg_data = preprocess_input(iimg_data)

inceptionV3_feature = applications.InceptionV3(weights='imagenet',
                                            include_top=False,
                                            input_shape=(299, 299, 3))

ifeature = inceptionV3_feature.predict(iimg_data)
K.clear_session()
ifeature = np.reshape(ifeature, ifeature.shape[1:])


# resnet50 ensemble
x = np.expand_dims(rfeature, axis=0)

r_model_AK = load_model("finalModel/resnet50/CV4_AK_weight_best.hdf5",
                        custom_objects={'f1': f1})
rfeature_AK = r_model_AK.predict(x)
K.clear_session()
r_model_BCC = load_model("finalModel/resnet50/CV1_BCC_weight_best.hdf5",
                         custom_objects={'f1': f1})
rfeature_BCC = r_model_BCC.predict(x)
K.clear_session()
r_model_BKL = load_model("finalModel/resnet50/CV1_BKL_weight_best.hdf5",
                         custom_objects={'f1': f1})
rfeature_BKL = r_model_BKL.predict(x)
K.clear_session()
r_model_DF = load_model("finalModel/resnet50/CV3_DF_weight_best.hdf5",
                        custom_objects={'f1': f1})
rfeature_DF = r_model_DF.predict(x)
K.clear_session()
r_model_MEL = load_model("finalModel/resnet50/CV1_MEL_weight_best.hdf5",
                         custom_objects={'f1': f1})
rfeature_MEL = r_model_MEL.predict(x)
K.clear_session()
r_model_NV = load_model("finalModel/resnet50/CV1_NV_weight_best.hdf5",
                        custom_objects={'f1': f1})
rfeature_NV = r_model_NV.predict(x)
K.clear_session()
r_model_SCC = load_model("finalModel/resnet50/CV4_SCC_weight_best.hdf5",
                         custom_objects={'f1': f1})
rfeature_SCC = r_model_SCC.predict(x)
K.clear_session()
r_model_VASC = load_model("finalModel/resnet50/CV3_VASC_weight_best.hdf5",
                          custom_objects={'f1': f1})
rfeature_VASC = r_model_VASC.predict(x)
K.clear_session()



resnet50_feature = np.vstack((rfeature_AK, rfeature_BCC, rfeature_BKL,rfeature_DF, rfeature_MEL, rfeature_NV, rfeature_SCC, rfeature_VASC))

resnet50_feature = resnet50_feature.flatten()


# resnet50_feature = resnet50_model.predict(rfeature_output)

# inceptionV3 ensemble
y = np.expand_dims(ifeature, axis=0)

i_model_AK = load_model("finalModel/inceptionV3/AK_weights.best.hdf5.CV1",
                        custom_objects={'f1': f1})
ifeature_AK = i_model_AK.predict(y)
K.clear_session()
i_model_BCC = load_model("finalModel/inceptionV3/BCC_weights.best.hdf5.CV3",
                         custom_objects={'f1': f1})
ifeature_BCC = i_model_BCC.predict(y)
K.clear_session()
i_model_BKL = load_model("finalModel/inceptionV3/BKL_weights.best.hdf5.CV5",
                         custom_objects={'f1': f1})
ifeature_BKL = i_model_BKL.predict(y)
K.clear_session()
i_model_DF = load_model("finalModel/inceptionV3/DF_weights.best.hdf5.CV2",
                        custom_objects={'f1': f1})
ifeature_DF = i_model_DF.predict(y)
K.clear_session()
i_model_MEL = load_model("finalModel/inceptionV3/MEL_weights.best.hdf5.CV3",
                         custom_objects={'f1': f1})
ifeature_MEL = i_model_MEL.predict(y)
K.clear_session()
i_model_NV = load_model("finalModel/inceptionV3/NV_weights.best.hdf5.CV3",
                        custom_objects={'f1': f1})
ifeature_NV = i_model_NV.predict(y)
K.clear_session()
i_model_SCC = load_model("finalModel/inceptionV3/SCC_weights.best.hdf5.CV5",
                         custom_objects={'f1': f1})
ifeature_SCC = i_model_SCC.predict(y)
K.clear_session()
i_model_VASC = load_model("finalModel/inceptionV3/VASC_weights.best.hdf5.CV3",
                          custom_objects={'f1': f1})
ifeature_VASC = i_model_VASC.predict(y)
K.clear_session()


inceptionV3_feature = np.vstack((ifeature_AK, ifeature_BCC, ifeature_BKL,ifeature_DF, ifeature_MEL, ifeature_NV, ifeature_SCC, ifeature_VASC))

inceptionV3_feature = inceptionV3_feature.flatten()


# inceptionV3_feature = inceptionV3_model.predict(ifeature_output)

# finalEnsemble


resnet50_feature = np.expand_dims(resnet50_feature, axis=0)
print resnet50_feature
resnet50Ensmeble = load_model("finalModel/resnet50Best.hdf5",
                              custom_objects={'f1': f1})
finalr = resnet50Ensmeble.predict(resnet50_feature)
K.clear_session()
inceptionV3_feature = np.expand_dims(inceptionV3_feature, axis=0)
print inceptionV3_feature
inceptionV3Ensmeble = load_model("finalModel/inceptionV3Best.hdf5",
                                 custom_objects={'f1': f1})
finali = inceptionV3Ensmeble.predict(inceptionV3_feature)
K.clear_session()
finalFeature = np.vstack((finalr, finali))
print finalFeature
finalFeature = finalFeature.flatten()
finalFeature = np.expand_dims(finalFeature, axis=0)
print finalFeature.shape

finalModel = load_model("finalModel/iAndR_allBest.hdf5",
                        custom_objects={'f1': f1})


output = finalModel.predict(finalFeature)
print output
end_time = time.time()
print 'cost time: {0}'.format(end_time-start_time)
con = MySQLdb.Connect(host='140.127.220.106',
                     port=3306,
                     user='skindb',
                     passwd='gEqM9v9kndcVGjXf',
                     db='webTest',
                     charset='utf8')

sql_insert = ("INSERT INTO history(`NO`,`AK`,`BCC`,`BKL`,`DF`,`MEL`,`NV`,`SCC`,`VASC`)"  "VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)")
sql_data = (output[0], output[1], output[2], output[3],
           output[4], output[5], output[6], output[7])
con.execute(sql_insert, sql_data)
con.commit()
con.close()

