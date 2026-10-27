
import numpy as np

def gaussian_elimination(A, b):

    
    A = np.array(A, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True).reshape(-1)

    
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A must be a square matrix")

    n = A.shape[0]

    if b.size != n:
        raise ValueError("b must have n elements")

    
    for k in range(n - 1):

        
        pivot_row = k + np.argmax(np.abs(A[k:, k]))

        if abs(A[pivot_row, k]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular")

        if pivot_row != k:
            A[[k, pivot_row], :] = A[[pivot_row, k], :]
            b[[k, pivot_row]] = b[[pivot_row, k]]

        for i in range(k + 1, n):

            factor = A[i, k] / A[k, k]

            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]

    
    x = np.zeros(n, dtype=float)

    for i in range(n - 1, -1, -1):

        if abs(A[i, i]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular")

        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x
