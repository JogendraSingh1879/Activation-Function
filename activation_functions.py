# -*- coding: utf-8 -*-
"""Activation Functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Ask2fetP5_3iXPFm5tbxaL2TUYwOX1U
"""

# Importing important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import h5py

# Activation Functions
def sigmoid(Z):
    A = 1 / (1 + np.exp(-Z))
    return A, Z

def tanh(Z):
  A = np.tanh(Z)
  return A, Z

def relu(Z):
  A = np.maximum(0, Z)
  return A, Z

def leaky_relu(Z):
    A = np.maximum(0.01 * Z, Z)
    return A, Z

# Plotting 4 activation functions
Z = np.linspace(-10, 10, 100)

# Computing post activation outputs
A_sigmoid, Z = sigmoid(Z)
A_tanh, Z = tanh(Z)
A_relu, Z = relu(Z)
A_leaky_relu, Z = leaky_relu(Z)

# Plotting sigmoid
plt.figure(figsize = (12, 7))
plt.subplot(2, 2, 1)
plt.plot(Z, A_sigmoid, label = 'Function')
plt.plot(Z, A_sigmoid * (1 - A_sigmoid), label = 'Derivative')
plt.title('Sigmoid Function', fontsize = 16)
plt.legend('upper left')
plt.xlabel('Z')
plt.ylabel(r"$frac{1}{1 + e^{-Z}}$}")

# Plotting tanh
plt.subplot(2, 2, 2)
plt.plot(Z, A_tanh, 'b', label = 'Function')
plt.plot(Z, 1 - np.square(A_tanh), 'r', label = 'Derivative')
plt.title('Tanh Function', fontsize = 16)
plt.legend('upper left')
plt.xlabel('Z')
plt.ylabel(r"$frac{e^{Z} - e^{-Z}}{e^{Z} + e^{-Z}}$")

# Plotting relu
plt.subplot(2, 2, 3)
plt.plot(Z, A_relu, 'g', label = 'Function')
plt.xlabel('Z')
plt.ylabel(r"$max(0, Z)$")
plt.title('ReLU Function', fontsize = 16)
plt.legend('upper left')

# Plotting leaky relu
plt.subplot(2, 2, 4)
plt.plot(Z, A_leaky_relu, 'y', label = 'Function')
plt.xlabel('Z')
plt.ylabel(r"$max(0.01Z, Z)$")
plt.title('Leaky ReLU Function', fontsize = 16)
plt.legend('upper left')

plt.tight_layout();
