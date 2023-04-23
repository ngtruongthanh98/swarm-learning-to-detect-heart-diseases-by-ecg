import keras
print(keras.__version__)
import tensorflow as tf
print('test: ',tf.config.list_physical_devices('GPU'))  