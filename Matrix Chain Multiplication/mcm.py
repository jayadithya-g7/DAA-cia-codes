import math

def matrix_chain_multiplication(dimensions: list[int]) -> tuple[int, list[tuple[int, int]]]:   #til, tii
    """
    Finds the minimum number of scalar multiplications needed to multiply a chain of matrices
    and the optimal parenthesization.

    Args:
        dimensions: A list of integers representing the dimensions of the matrices.
                   If the matrices are A1, A2, ..., An, then dimensions will be
                   [p0, p1, p2, ..., pn], where Ai has dimensions pi-1 x pi.

    Returns:
        A tuple containing:
            - The minimum number of scalar multiplications (int).
            - A list of tuples representing the optimal split points for parenthesization
              (optional, can be left as an empty list if only the cost is required).
              Each tuple (i, j, k) would indicate that the optimal split for the
              matrix chain from Ai to Aj occurs at Ak.
    """
    n = len(dimensions) - 1  # Number of matrices
    # dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    mulTable = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            for k in range(i, j):
                q = mulTable[i][k] + mulTable[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < mulTable[i][j]:
                    mulTable[i][j] = q
                    s[i][j] = k 
    


    ## YOUR CODE GOES HERE

    ##
    ## Print the minimum number of multiplications involved.
    return mulTable[0][n-1], s


p = [5, 10, 15, 20, 25]

print(matrix_chain_multiplication(p))
