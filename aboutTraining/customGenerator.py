import numpy as np
import keras
import os

class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, folder, classDict, batch_size=32, dim=(32,32,32),
                 shuffle=True):
        'Initialization'
        self.dim = dim
        self.batch_size = batch_size
        self.n_classes = len(classDict)
        self.shuffle = shuffle
        self.folder = folder
        self.classDict = classDict

        self.className = dict()

        for key in classDict:
            self.className[classDict[key]] = key

        self.list_IDs = list()
        self.labels = dict()
        for className in os.listdir(self.folder):
            for npyName in os.listdir(self.folder + '/' + className + '/'):
                self.list_IDs.append(npyName)
                self.labels[npyName] = self.classDict[className]

        print("%s has %d items and %d classes." %(self.folder, len(self.list_IDs), self.n_classes))

        self.on_epoch_end()

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.list_IDs) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        # Find list of IDs
        list_IDs_temp = [self.list_IDs[k] for k in indexes]

        # Generate data
        X, y = self.__data_generation(list_IDs_temp)

        return X, y

    def __data_generation(self, list_IDs_temp):
        'Generates data containing batch_size samples' # X : (n_samples, *dim, n_channels)
        # Initialization
        dimPair =[self.batch_size]
        for i in self.dim:
            dimPair.append(i)
        dimPair = tuple(dimPair)

        X = np.empty(dimPair)
        y = np.empty((self.batch_size), dtype=int)

        # Generate data
        for i, ID in enumerate(list_IDs_temp):
            # Store class
            y[i] = self.labels[ID]

            # Store sample
            X[i,] = np.load(self.folder + '/' + self.className[y[i]] + '/' + ID)

        return X, keras.utils.to_categorical(y, num_classes=self.n_classes)
