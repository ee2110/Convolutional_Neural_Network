# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:17:19 2020

@author: user
"""

	
import tensorflow as tf
from tensorflow import keras
import tensorflowjs as tfjs
import numpy as np
import matplotlib.pyplot as plt

epoch = 2
# split the mnist data into train and test
(train_data,train_label),(test_data,test_label) = keras.datasets.mnist.load_data()

# reshape and scale the data
train_data = train_data.reshape([-1, 28, 28, 1])
test_data = test_data.reshape([-1, 28, 28, 1])
train_data = train_data/255.0
test_data = test_data/255.0
 
# convert class vectors to binary class matrices --> one-hot encoding
train_label = keras.utils.to_categorical(train_label)
test_label = keras.utils.to_categorical(test_label)

model = keras.Sequential([
    keras.layers.Conv2D(32, (5, 5), padding="same", input_shape=[28, 28, 1]),
    keras.layers.MaxPool2D((2,2)),
    
    keras.layers.Conv2D(64, (5, 5), padding="same"),
    keras.layers.MaxPool2D((2,2)),
    
    keras.layers.Flatten(),
    keras.layers.Dense(1024, activation='relu'),
    
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_data, train_label, validation_data=(test_data, test_label), epochs=epoch)


# Plot loss history
plt.subplot(211)
plt.title('Loss')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend(loc="upper left")
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.xticks(range(min(epoch), max(epoch)+1))
plt.show()

# Plot accuracy history
plt.subplot(212)
plt.title('Accuracy')
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='test')
plt.legend(loc="upper left")
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.xticks(range(min(epoch), max(epoch)+1))
plt.show()

#tfjs.converters.save_keras_model(model, 'simple_CNN_models')