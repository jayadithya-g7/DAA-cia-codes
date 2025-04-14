import numpy as np


def split(A : np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    mid = A.shape[0] // 2
    return A[:mid,:mid], A[:mid,mid:], A[mid:,:mid], A[mid:,mid:]


def combine(A : np.ndarray, B : np.ndarray, C : np.ndarray, D : np.ndarray):
    top = np.hstack((A, B))
    bottom = np.hstack((C, D))
    return np.vstack((top, bottom))


def strassen_matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Multiplies two square matrices A and B using Strassen’s divide and conquer method.
    Assumes the dimensions of A and B are n x n, where n is a power of 2.

    Args:
        A: The first square matrix (NumPy array).
        B: The second square matrix (NumPy array).

    Returns:
        The product of A and B as a NumPy array.
    """
    n = A.shape[0]

    if n == 1:
        return A*B

    a, b, c, d = split(A)
    e, f, g, h = split(B)

    p1 = strassen_matrix_multiply(a+d, e+h)
    p2 = strassen_matrix_multiply(d, g-e)
    p3 = strassen_matrix_multiply(a+b, h)
    p4 = strassen_matrix_multiply(b-d, g+h)
    p5 = strassen_matrix_multiply(a, f-h)
    p6 = strassen_matrix_multiply(c+d, e)
    p7 = strassen_matrix_multiply(a-c, e+f)


    q1 = p1 + p2 - p3 + p4
    q2 = p5 + p3
    q3 = p6 + p3
    q4 = p5 + p1 - p6 - p7

    return combine(q1, q2, q3, q4)


a1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
]

b1 = [
    [1, 0, 2, 1],
    [0, 1, 0, 2],
    [1, 0, 1, 0],
    [0, 3, 2, 1]
]

print(*strassen_matrix_multiply(np.array(a1), np.array(b1)).tolist(), sep="\n")
