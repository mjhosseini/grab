This is the implementation for the following paper:

Learning Sparse Gaussian Graphical Models with Overlapping Blocks‎, Mohammad Javad Hosseini and Su-In Lee. Neural Information Processing Systems (NIPS), 2016.

You should have R and the R package quic installed on your machine. The file main.py shows an example and will get you started. It uses MILE data (AML
cancer dataset) as input. We have selected 500 genes, consisting of 488 highest varying genes in MILE and 12 genes highly associated with AML:
FLT3, NPM1, CEBPA, KIT, N-RAS, MLL, WT1, IDH1/2, TET2, DNMT3A, and ASXL1. Please see data/genes.mat.

The usage is as follows:

(Theta, blocks) = grab.BCD(S,lmbda,K,o_size,max_iter,tol,dual_max_iter,dual_tol)

Inputs:

S: p by p covariance matrix (p is the number of variables; The data itself should be normalized)

lmbda: The regularization parameter

K: The number of blocks

o_size: The average overlap size for blocks

max_iter: The maximum number of iterations for the main BCD

tol: Threshold for convergence of the main BCD

max_iter_tol: The maximum number of iterations for the dual problem

dual_tol: Threshold for the convergence of the dual problem

Outputs:

Theta: Learned inverse covariance matrix

blocks: Learned overlapping blocks

Please email the first author (hosseini@cs.washington.edu) in case of any questions and/or requests.
