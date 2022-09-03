from typing import *
import itertools
import numpy as np
import sys

input = sys.stdin.readline


def main():
    M, N = map(int, input().split())
    K: int = int(input())
    G: np.ndarray = np.array([list(input()) for i in range(M)])
    G = np.pad(G, (1, 0))
    A, B, C, D = map(
        np.array, zip(*[list(map(int, input().split())) for i in range(K)])
    )
    A -= 1
    B -= 1

    J = (G == "J").cumsum(axis=0).cumsum(axis=1)
    O = (G == "O").cumsum(axis=0).cumsum(axis=1)

    a: int = J[C, D] - J[C, B] - J[A, D] + J[A, B]
    b: int = O[C, D] - O[C, B] - O[A, D] + O[A, B]
    c: int = (D - B) * (C - A) - a - b
    for j, o, i in zip(a, b, c):
        print(j, o, i)


if __name__ == "__main__":
    main()
