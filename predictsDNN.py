# predict
# to test this code I advice running it in Google colab 
import tensorflow as tf
import numpy as np
from keras.layers import LSTM, Dense
from tensorflow import keras

#This data has to be rearanged it's not in the best format possible
input = [4.62, 1.36, 1.80, 1.00, 1.31, 1.14, 1.72, 3.93, 48.33, 2.05, 1.72, 19.02, 2.86, 1.19, 1.00, 1.00, 1.14, 7.67, 7.63, 1.54, 2.35, 3.82, 1.90, 1.01, 1.89, 3.98, 1.19, 1.23, 3.43, 4.75, 14.82, 6.02]
output = [1.49, 3.32, 4.19, 15.35, 2.93, 6.83, 1.16, 2.00, 1.23, 1.48, 1.38, 1.22, 2.30, 1.02, 1.97, 1.54, 2.24, 1.10, 1.19, 2.46, 5.59, 8.81, 1.51, 4.54, 1.07, 1.31, 1.11, 3.05, 1.16, 1.23, 2.07, 1.08]
input = np.array(input)
output = np.array(output)

#initiate layers and play around with them to define the number of layers that give better accuracy
my_layer_1 = keras.layers.Dense(units=1000, input_shape=[1])
my_layer_2 = keras.layers.Dense(units=400, activation='relu')
my_layer_3 = keras.layers.Dense(units=6, activation='relu')
#my_layer_4 = keras.layers.Dense(units=12, activation='tanh')
#my_layer_5 = keras.layers.Dense(units=8, activation='tanh')
#my_layer_6 = keras.layers.Dense(units=4, activation='tanh')
my_layer_7 = keras.layers.Dense(units=3)

#make model
# to initaite all layers line uncomment the commented layers and change to the appropriate model 
#model = tf.keras.Sequential([my_layer_1, my_layer_2, my_layer_3, my_layer_4, my_layer_5, my_layer_6, my_layer_7])
model = tf.keras.Sequential([my_layer_1, my_layer_2, my_layer_3, my_layer_7])
"""
model = Sequential()
model.add(tf.keras.layers.Dense(4, input_shape=[1]))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
"""
model.compile(optimizer='Adam', loss='mse')
model.fit(input, output, steps_per_epoch=20, epochs=500)
# input the next number to be predicted
print(model.predict([2.07]))