import matplotlib

matplotlib.use('Agg')

import numpy as np
import pway_funcs as fn2
import scipy.io
import GRAB as grab

K = 10
o_size = .3#The size of overlap, as an input parameter
maxIter = 2
lmbda = .2

train = scipy.io.loadmat("data/genes.mat")['train']
train = fn2.standardize(train)
data = train
data = data.T

print "data: ", data

S = np.cov(data)
(Theta, blocks) = grab.BCD(S,maxIter=maxIter,lmbda=lmbda,k_in=K,o_size=o_size)
print "Theta: ", Theta
print "Overlappign Blocks: ", blocks





