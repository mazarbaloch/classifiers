import numpy as np
import cv2

# initialize the class labels and set the seed of the pseudorandom
# number generator so we can reproduce our results

labels = ["dog","cat","panda"]
np.random.seed(1)

# randomly initialize our weight matrix and bias vector -- in a
# *real* training and classification task, these parameters would
# be *learned* by our model, but for the sake of this example,
# let’s use random values

W = np.random.randn(3,3072)
b = np.random.randn(3)