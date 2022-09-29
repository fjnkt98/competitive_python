from typing import *
import collections
import itertools
import bisect
import math
import numpy as np


def matrix_power(A: np.ndarray, n: int, mod: int) -> np.ndarray:
    if n == 0:
        return np.eye(A.shape[0])
    if n == 1:
        return A
    if n % 2 == 1:
        return np.dot(A, matrix_power(A, n - 1, mod) % mod) % mod

    B = matrix_power(A, n // 2, mod) % mod
    return np.dot(B, B) % mod


def main():
    N, K = map(int, input().split())
    A: np.ndarray = np.array(
        [list(map(int, input().split())) for i in range(N)], dtype="O"
    )
    mod: int = 1000000007

    D = matrix_power(A, K, mod)
    answer: int = 0
    for i, j in itertools.product(range(N), repeat=2):
        answer += D[i, j]
        answer %= mod
    print(answer)


if __name__ == "__main__":
    main()
