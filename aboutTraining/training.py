import numpy as np # linear algebra
import os
from PIL import Image
from skimage.transform import resize
from random import shuffle
from customGenerator import DataGenerator
from keras import backend as K
import tensorflow as tf

from keras.preprocessing.image import ImageDataGenerator
from keras.applications.resnet50 import preprocess_input

from keras.models import Sequential
from keras.models import Model
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, EarlyStopping, ReduceLROnPlateau, TensorBoard, CSVLogger
from keras import optimizers, losses, activations, models
from keras.layers import Convolution2D, Dense, Input, Flatten, Dropout, MaxPooling2D, BatchNormalization, GlobalAveragePooling2D, Concatenate
from keras import applications

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

    """
    ###micro version
    tp = K.sum(K.sum(K.cast(y_true*y_pred, 'float'), axis=0))
    tn = K.sum(K.sum(K.cast((1-y_true)*(1-y_pred), 'float'), axis=0))
    fp = K.sum(K.sum(K.cast((1-y_true)*y_pred, 'float'), axis=0))
    fn = K.sum(K.sum(K.cast(y_true*(1-y_pred), 'float'), axis=0))

    p = tp / (tp + fp + K.epsilon())
    r = tp / (tp + fn + K.epsilon())

    f1 = 2*p*r / (p+r+K.epsilon())
    return f1
    """

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.ConfigProto()
config.gpu_options.allow_growth = True 
config.gpu_options.per_process_gpu_memory_fraction = 0.7

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = "%.1f" % (100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

#### do not show warning and deprecated message
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
try:
    from tensorflow.python.util import module_wrapper as deprecation
except ImportError:
    from tensorflow.python.util import deprecation_wrapper as deprecation
deprecation._PER_MODULE_WARNING_LIMIT = 0

##### constants
my_dpi = 100

learningRate = 5e-4
imageSize = 224
epochNumber = 40
weightFile ="AK_weight_best.hdf5"
numberTrain = 20265
numberVal = 5066
batchSize = 512
## {'BKL': 2, 'MEL': 4, 'AK': 0, 'SCC': 6, 'BCC': 1, 'DF': 3, 'VASC': 7, 'NV': 5}
#classWeight = {0: 14, 1: 4, 2: 5, 3: 53, 4: 3, 5: 1, 6: 20, 7: 50}

## {'VASC': 1, 'Other': 0}
classWeight = {0: 1, 1: 30}
classDict = {'0_Other':0, 'AK': 1}
dataFolder = 'AK_CV_resize_224/'
Fold = 5
inputSize = (7, 7, 2048)

for i in range(Fold):
    CV = "CV" + str(i+1)
    file_path=  CV+"_"+weightFile
    
    #train_idg = ImageDataGenerator(vertical_flip=True,
    #                               horizontal_flip=True,
    #                               height_shift_range=0.1,
    #                               width_shift_range=0.1,
    #                               preprocessing_function=preprocess_input)
    """
    train_idg = ImageDataGenerator()
    train_gen = train_idg.flow_from_directory(
        dataFolder + CV +"/training",
        batch_size = batchSize,
        target_size=(imageSize, imageSize),
        class_mode = "categorical"
    )

    val_idg = ImageDataGenerator()
    val_gen = val_idg.flow_from_directory(
        dataFolder + CV +"/val",
        batch_size = batchSize,
        target_size=(imageSize, imageSize),
        class_mode = "categorical"
    )
    """
    params = {'dim': inputSize,
              'batch_size': batchSize,
              'shuffle': True}

    train_gen = DataGenerator(
        dataFolder + CV +"/training", classDict,
        **params
    )
    val_gen = DataGenerator(
        dataFolder + CV +"/val", classDict,
        **params
    )

    add_model = Sequential()
    add_model.add(Convolution2D(2048, 1, 1, input_shape = inputSize, activation = 'relu'))
#     add_model.add(Flatten())
    add_model.add(GlobalAveragePooling2D())
    add_model.add(Dropout(0.58))
    add_model.add(BatchNormalization())
    add_model.add(Dense(32, 
                        activation='tanh',
                        kernel_initializer='glorot_normal'))
    add_model.add(Dropout(0.58))
    add_model.add(BatchNormalization())
    add_model.add(Dense(32, 
                        activation='sigmoid',
                        kernel_initializer='glorot_normal'))
    add_model.add(Dropout(0.58))
    add_model.add(BatchNormalization())
    add_model.add(Dense(32, 
                        activation='sigmoid',
                        kernel_initializer='glorot_normal'))
    add_model.add(Dropout(0.58))
#     add_model.add(BatchNormalization())
#     add_model.add(Dense(16, 
#                         activation='tanh',
#                         kernel_initializer='glorot_normal'))
#     add_model.add(Dropout(0.75))
    add_model.add(Dense(len(classDict), 
                        activation='softmax',
                        kernel_initializer='glorot_normal'))

    model = add_model
    model.save_weights('my_model_weights.h5')
    model.compile(loss='categorical_crossentropy', 
#                   optimizer=optimizers.RMSprop(lr=learningRate, rho = 0.9),
                  optimizer=optimizers.Adam(lr=learningRate, decay=1e-5, beta_1=0.9, beta_2=0.999, amsgrad=False),
                  metrics=['accuracy', f1])
    model.summary()


    checkpoint = ModelCheckpoint(file_path, monitor='val_f1', verbose=1, save_best_only=True, mode='max')

    early = EarlyStopping(monitor="val_acc", mode="max", patience=40)
    
    csv_logger = CSVLogger("history/cv"+str(i+1)+"_history_log.csv", append=True)

    callbacks_list = [checkpoint, early, csv_logger] #early

    history = model.fit_generator(train_gen, 
                                  epochs=epochNumber, 
                                  class_weight = classWeight,
                                  shuffle=True, 
                                  verbose=True,
                                  steps_per_epoch= numberTrain // batchSize,
                                  callbacks=callbacks_list,
                                  validation_data=val_gen,
                                  validation_steps = numberVal // batchSize,
                                  use_multiprocessing=False,
                                  #workers=3
                                  )


    model.load_weights('my_model_weights.h5')