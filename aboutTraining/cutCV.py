import os
import PIL.Image
import csv
import numpy as np
from sklearn.model_selection import StratifiedKFold

from keras import applications
from keras.models import Sequential
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input
from keras.applications.inception_v3 import InceptionV3

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
try:
    from tensorflow.python.util import module_wrapper as deprecation
except ImportError:
    from tensorflow.python.util import deprecation_wrapper as deprecation
deprecation._PER_MODULE_WARNING_LIMIT = 0

width = 299
size = (width, width)
foldNumber = 5

focusType = "NV"

##### read in label

labelFile = "label/ISIC_2019_Training_GroundTruth.csv"
labelDict = dict()

with open(labelFile, 'r') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        category = ""
        for key in row.keys():
            if row[key] == "1.0":
                category = key
                break
        if category == focusType:        
            labelDict[row['image']] = category
        else:
            labelDict[row['image']] = "0_Other"


#### read the image file name

list_paths = []
for subdir, dirs, files in os.walk("train/ISIC_2019_Training_Input"):
    for fileName in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + fileName
        list_paths.append(filepath)

labelList = [labelDict[x.split(os.sep)[-1].split(".")[0]] for x in list_paths]

#### stratified k fold

skf = StratifiedKFold(n_splits=foldNumber, shuffle = True)
count = 1

model = applications.InceptionV3(weights='imagenet',
                                 include_top=False,
                                 input_shape=(width, width, 3))
model.summary()

for train_index, test_index in skf.split(list_paths, labelList):
    CV = "CV" + str(count)
    CVFolder = focusType + "_CV_resize_" + str(width) + "/" + CV + ""
    if not os.path.exists(CVFolder):
        os.makedirs(CVFolder)
        os.makedirs(CVFolder + "/training")
        os.makedirs(CVFolder + "/val")

    for index in train_index:
        imageName = list_paths[index]
        outputName = imageName.split(os.sep)[-1].split(".")[0]
        directory = labelDict[outputName]
        if not directory == labelList[index]:
            print "error", imageNa,e
        
        #print imageName, outputName, directory
        
        if not os.path.exists(CVFolder + "/training/" + directory):
            os.makedirs(CVFolder + "/training/" + directory)

        img = image.load_img(imageName, target_size=size)
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)

        feature = model.predict(img_data)
        feature = np.reshape(feature, feature.shape[1:])
        np.save(CVFolder + "/training/" + directory + "/"+ outputName, feature)

        #im = PIL.Image.open(image)
        #im.thumbnail(size, PIL.Image.ANTIALIAS)

        #im.save(CVFolder + "/training/" + directory + "/"+ outputName + ".jpg", "JPEG")

    for index in test_index:
        imageName = list_paths[index]
        outputName = imageName.split(os.sep)[-1].split(".")[0]
        directory = labelDict[outputName]
        if not directory == labelList[index]:
            print "error", imageName
        
        #print imageName, outputName, directory
        
        if not os.path.exists(CVFolder + "/val/" + directory):
            os.makedirs(CVFolder + "/val/" + directory)

        img = image.load_img(imageName, target_size=size)
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)

        feature = model.predict(img_data)
        feature = np.reshape(feature, feature.shape[1:])
        np.save(CVFolder + "/val/" + directory + "/"+ outputName, feature)
        #im = PIL.Image.open(image)
        #im.thumbnail(size, PIL.Image.ANTIALIAS)
        #im.save(CVFolder + "/val/" + directory + "/"+ outputName + ".jpg", "JPEG")
    count += 1

