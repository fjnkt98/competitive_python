from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def matrix_multiply(A: np.ndarray, B: np.ndarray, mod: int):
    C: np.ndarray = A @ B
    C %= mod

    return C


def matrix_power(A: np.ndarray, N: int, mod: int):
    P = A.copy()
    Q = np.zeros(3)
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

    mod: int = 1000000007

    A = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
    B = matrix_power(A, N - 1, mod)
    answer: int = np.dot(B[2], np.array([2, 1, 1]))
    answer %= mod
    print(answer)


if __name__ == "__main__":
    main()
