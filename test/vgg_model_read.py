import tensorflow as tf
import numpy as np
import settings
import scipy.io

# MODEL_PATH = '../imagenet-vgg-verydeep-19.mat'
# vgg = scipy.io.loadmat(MODEL_PATH)
# layers = vgg.get('layers')
#
# print(type(layers[0][0][0][0][0][0]))
# print(np.shape(layers[0][0][0][0][0][0][0][1]))
# print(layers[0][0][0][0][0][0][0][1])

t = [('conv4_2', 0.5), ('conv5_2', 0.5)]

for i, j in t:
	print(type(j))
