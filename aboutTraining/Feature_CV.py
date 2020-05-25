import os
import PIL.Image
import csv
import numpy as np
from sklearn.model_selection import StratifiedKFold

from keras import applications
from keras.models import Sequential
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from keras.applications.resnet50 import ResNet50

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
try:
    from tensorflow.python.util import module_wrapper as deprecation
except ImportError:
    from tensorflow.python.util import deprecation_wrapper as deprecation
deprecation._PER_MODULE_WARNING_LIMIT = 0

width = 224
size = (width, width)
foldNumber = 5


##### read in label

labelFile = "/home/thyang/ISIC2019/label/ISIC_2019_Training_GroundTruth.csv"
labelDict = dict()

with open(labelFile, 'r') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        category = ""
        for key in row.keys():
            if row[key] == "1.0":
                category = key
                break
        if category == 'AK':        
            labelDict[row['image']] = 'AK'
        elif category == 'BCC':        
            labelDict[row['image']] = 'BCC'
        elif category == 'BKL':        
            labelDict[row['image']] = 'BKL'
        elif category == 'DF':        
            labelDict[row['image']] = 'DF'
        elif category == 'NV':        
            labelDict[row['image']] = 'NV'
        elif category == 'MEL':        
            labelDict[row['image']] = 'MEL'
        elif category == 'SCC':        
            labelDict[row['image']] = 'SCC'
        elif category == 'VASC':        
            labelDict[row['image']] = 'VASC'
        else:
            pass

        
#### read the image file name

list_paths = []
for subdir, dirs, files in os.walk("ensembleFeature"):
    for fileName in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + fileName
        list_paths.append(filepath)

labelList = [labelDict[x.split(os.sep)[-1].split(".")[0]] for x in list_paths]

#### stratified k fold

skf = StratifiedKFold(n_splits=foldNumber, shuffle = True)
count = 1

for train_index, test_index in skf.split(list_paths, labelList):
    CV = "CV" + str(count)
    CVFolder = "ensembleFeature_CV/" + CV + ""
    if not os.path.exists(CVFolder):
        os.makedirs(CVFolder)
        os.makedirs(CVFolder + "/training")
        os.makedirs(CVFolder + "/val")

    for index in train_index:
        npyName = list_paths[index]
        outputName = npyName.split(os.sep)[-1].split(".")[0]
        directory = labelDict[outputName]
        if not directory == labelList[index]:
            print "error", npyName
        
        #print imageName, outputName, directory
        
        if not os.path.exists(CVFolder + "/training/" + directory):
            os.makedirs(CVFolder + "/training/" + directory)

        x = np.load(npyName)

        np.save(CVFolder + "/training/" + directory + "/"+ outputName, x)

        #im = PIL.Image.open(image)
        #im.thumbnail(size, PIL.Image.ANTIALIAS)

        #im.save(CVFolder + "/training/" + directory + "/"+ outputName + ".jpg", "JPEG")

    for index in test_index:
        npyName = list_paths[index]
        outputName = npyName.split(os.sep)[-1].split(".")[0]
        directory = labelDict[outputName]
        if not directory == labelList[index]:
            print "error", npyName
        
        #print imageName, outputName, directory
        
        if not os.path.exists(CVFolder + "/val/" + directory):
            os.makedirs(CVFolder + "/val/" + directory)

        x = np.load(npyName)

        np.save(CVFolder + "/val/" + directory + "/"+ outputName, x)
        #im = PIL.Image.open(image)
        #im.thumbnail(size, PIL.Image.ANTIALIAS)
        #im.save(CVFolder + "/val/" + directory + "/"+ outputName + ".jpg", "JPEG")
    count += 1

