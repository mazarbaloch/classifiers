# import the necessary packages
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import argparse

def sigmoid_activation(x):
	#compute the sigmoid activation value for a given input
	return 1.0 / (1 + np.exp(-x))


def predict(X, W):
	# take the dot product between our features and weight matrix
	preds = sigmoid_activation(X.dot(W))

	# apply a step fucntion to threshold the outputs to binary
	# class labels 
	preds[preds <= 0.5] = 0
	preds[preds > 0.5] = 1

	#return the predictions
	return preds
def next_batch(X, y, batchSize):
	# loop over our dataset ‘X‘ in mini-batches, yielding a tuple of
	# the current batched data and labels
	for i in np.arange(0, X.shape[0], batchSize):
		yield (X[i:i + batchSize], y[i:i + batchSize])

