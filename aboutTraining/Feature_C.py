import csv
import shutil
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

target_path = "ensembleFeature_C"
original_path = "ensembleFeature"

if not os.path.exists(target_path):
        os.makedirs(target_path)
        os.makedirs(target_path + "/AK")
        os.makedirs(target_path + "/BCC")
        os.makedirs(target_path + "/BKL")
        os.makedirs(target_path + "/DF")
        os.makedirs(target_path + "/MEL")
        os.makedirs(target_path + "/NV")
        os.makedirs(target_path + "/SCC")
        os.makedirs(target_path + "/VASC")

with open('/home/thyang/ISIC2019/label/ISIC_2019_Training_GroundTruth.csv',"rt") as csvfile:
    reader = csv.reader(csvfile)
    rows= [row for row in reader]

    
    for row in rows:
        if(row[1]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/MEL/' + row[0] +'.npy')
        elif(row[2]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/NV/' + row[0] +'.npy')
        elif(row[3]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/BCC/' + row[0] +'.npy')
        elif(row[4]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/AK/' + row[0] +'.npy')
        elif(row[5]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/BKL/' + row[0] +'.npy')   
        elif(row[6]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/DF/' + row[0] +'.npy')
        elif(row[7]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/VASC/' + row[0] +'.npy')
        elif(row[8]=='1.0'):
            if(os.path.exists(original_path + '/' + row[0] + '.npy')):
                shutil.copy(original_path + '/' + row[0] + '.npy', target_path + '/SCC/' + row[0] +'.npy')
        else:
            pass