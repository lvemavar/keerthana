# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bJGlfOFaFQ-PnxyVoxttD7yCKUaDF_Jy
"""

#Importing all required modules


import os
from operator import itemgetter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from keras import models, regularizers, layers, optimizers, losses, metrics
from keras.models import Sequential
from keras.layers import Dense


from keras.datasets import imdb

#load IMDB dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
num_words=10000)


#Vectorizing the data

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')
print("y_train ", y_train.shape)
print("y_test ", y_test.shape)

#validation set

x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

#Building model using two hidden layer with 16 hidden units and relu activation function

model = models.Sequential()
model.add(layers.Dense(16,  activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


#Compiling the model using rnsprob optimizer and binary crossentropy loss function


model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history = model.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results = model.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results ", results)
history_dict = history.history
history_dict.keys()




# plotting training and validation accuracy
plt.clf()
acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']
epochs = range(1, (len(history_dict['acc']) + 1))
plt.plot(epochs, acc_values, 'bo', label='Training acc')
plt.plot(epochs, val_acc_values, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# plotting training and validation loss

plt.clf()
history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1, (len(history_dict['loss']) + 1))
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Building model using one hidden layer with 16 hidden units and relu activation function


model_1 = models.Sequential()
model.add(layers.Dense(16,  activation='relu', input_shape=(10000,)))
model_1.add(layers.Dense(1, activation='sigmoid'))


model_1.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_1 = model_1.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_1 = model_1.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_1 ", results_1)
history_dict_1 = history_1.history
history_dict_1.keys()


#Building model using three hidden layer with 16 hidden units and relu activation function


model_2 = models.Sequential()
model_2.add(layers.Dense(16,  activation='relu', input_shape=(10000,)))
model_2.add(layers.Dense(16, activation='relu'))
model_2.add(layers.Dense(16, activation='relu'))
model_2.add(layers.Dense(1, activation='sigmoid'))


model_2.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_2 = model_2.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_2 = model_2.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_2 ", results_2)
history_dict_2 = history_2.history
history_dict_2.keys()





#Now lets try with 32 hidden units instead of 16 and one hidden layer


model_3 = models.Sequential()
model_3.add(layers.Dense(32,  activation='relu', input_shape=(10000,)))
model_3.add(layers.Dense(1, activation='sigmoid'))


model_3.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_3 = model_3.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_3 = model_3.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_3 ", results_3)
history_dict_3 = history_3.history
history_dict_3.keys()



#Now lets try with 64 units and one hidden layer



model_4 = models.Sequential()
model_4.add(layers.Dense(64,  activation='relu', input_shape=(10000,)))
model_4.add(layers.Dense(1, activation='sigmoid'))


model_4.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_4 = model_4.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_4 = model_4.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_4 ", results_4)
history_dict_4 = history_4.history
history_dict_4.keys()




#Now lets replace binary_crossentropy loss function with mse

model_5 = models.Sequential()
model_5.add(layers.Dense(16,  activation='relu', input_shape=(10000,)))
model_5.add(layers.Dense(1, activation='sigmoid'))

model_5.compile(optimizer='rmsprop', loss='mse', metrics=['acc'])

history_5 = model_5.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_5 = model_5.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_5 ", results_5)
history_dict_5 = history_5.history
history_dict_5.keys()



#Using tanh function instead of relu


model_6 = models.Sequential()
model_6.add(layers.Dense(16,  activation='tanh', input_shape=(10000,)))
model_6.add(layers.Dense(1, activation='sigmoid'))

model_6.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_6 = model_6.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_6= model_6.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_6 ", results_6)
history_dict_6 = history_6.history
history_dict_6.keys()

results_6  [0.4356374740600586, 0.8637199997901917]
text/plain
dict_keys(['loss', 'acc', 'val_loss', 'val_acc'])

#Using drop out for three hidden layers with 64 units, MSE loss function and RELU


model_7 = models.Sequential()
model_7.add(layers.Dense(16,  activation='relu', input_shape=(10000,)))
model.add(layers.Dropout(0.5))
model_7.add(layers.Dense(16, activation='relu'))
model.add(layers.Dropout(0.5))
model_7.add(layers.Dense(16, activation='relu'))
model.add(layers.Dropout(0.5))
model_7.add(layers.Dense(1, activation='sigmoid'))

model_7.compile(optimizer='rmsprop', loss='mse', metrics=['acc'])

history_7 = model_7.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_7= model_7.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_7 ", results_7)
history_dict_7 = history_7.history
history_dict_7.keys()



#one layer with drop out of 0.5

model_8 = models.Sequential()
model_8.add(layers.Dense(16,  activation='relu', input_shape=(10000,)))
model_8.add(layers.Dropout(0.5))
model_8.add(layers.Dense(1, activation='sigmoid'))

model_8.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_8 = model_8.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_8= model_8.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_8 ", results_8)
history_dict_8 = history_8.history
history_dict_8.keys()



#Using l1 regulariser

model_9 = models.Sequential()
model_9.add(layers.Dense(64,  activation='relu', activity_regularizer = regularizers.L1(0.01),input_shape=(10000,)))
model_9.add(layers.Dense(1, activation='sigmoid'))


model_9.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_9 = model_9.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_9= model_9.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_9 ", results_9)
history_dict_9 = history_9.history
history_dict_9.keys()



#Using l2 regulariser


model_10 = models.Sequential()
model_10.add(layers.Dense(64,  activation='relu', activity_regularizer = regularizers.L2(0.01),input_shape=(10000,)))
model_10.add(layers.Dense(1, activation='sigmoid'))

model_10.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_10 = model_10.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_10= model_10.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_10 ", results_10)
history_dict_10 = history_10.history
history_dict_10.keys()


#Using adam optimizer instead of rmsprop


model_11= models.Sequential()
model_11.add(layers.Dense(64,  activation='relu', activity_regularizer = regularizers.L1(0.01),input_shape=(10000,)))
model_11.add(layers.Dense(1, activation='sigmoid'))

model_11.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history_11 = model_11.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

results_11= model_11.evaluate(x_test, y_test)
print("_"*100)
print("Test Loss and Accuracy")
print("results_11 ", results_11)
history_dict_11 = history_11.history
history_dict_11.keys()

