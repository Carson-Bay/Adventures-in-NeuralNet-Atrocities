import numpy as np
from numba import jit

@jit(nopython=True)
def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))
    sig = np.minimum(sig, 0.9999)  # Set upper bound
    sig = np.maximum(sig, 0.0001)  # Set lower bound
    return sig
