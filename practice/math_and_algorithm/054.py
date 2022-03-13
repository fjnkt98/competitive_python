from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def matrix_multiply(A: np.matrix, B: np.matrix, mod: int):
    C = A.dot(B)
    C %= mod

    return C


def matrix_power(A: np.matrix, N: int):
    mod: int = 1000000000
    P = A.copy()
    Q = np.matrix([[0, 0], [0, 0]])
    flag: bool = False

    for i in range(60):
        if (N & 1 << i) != 0:
            if flag is False:
                Q = P.copy()
                flag = True
            else:
                Q = matrix_multiply(Q, P, mod)

        P = matrix_multiply(P, P, mod)

    return Q


def main():
    N: int = int(input())

    A = np.matrix([[1, 1], [1, 0]])
    B = matrix_power(A, N - 1)
    answer: int = B[1, 0] + B[1, 1]
    answer %= 1000000000
    print(answer)


if __name__ == "__main__":
    main()
