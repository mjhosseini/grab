This is the implementation for the following paper:

Learning Sparse Gaussian Graphical Models with Overlapping Blocks‎, Mohammad Javad Hosseini and Su-In Lee. Neural Information Processing Systems (NIPS), 2016.

You should have R and the R package quic installed on your machine. You can use the main.py file to get started.

The usage is as follows:

(Theta, blocks) = grab.BCD(S,lmbda,K,o_size,max_iter,tol,dual_max_iter,dual_tol)

Inputs:

S: p by p covariance matrix (The data itself should be normalized)

lmbda: The regularization parameter

K: The number of blocks

o_size: The average overlap size for blocks

max_iter: The maximum number of iterations for the main BCD

tol: Threshold for convergence of the main BCD

max_iter_tol: The maximum number of iterations for the dual problem

dual_tol: Threshold for the convergence of the dual problem


Outputs:

Theta: learned inverse covariance matrix

blocks: Learned overlapping blocks

Please email the first author (hosseini@cs.washington.edu) in case of any questions and/or requests.
