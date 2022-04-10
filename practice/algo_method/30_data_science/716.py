from typing import List, Tuple
import sys
import collections
import itertools
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: np.ndarray = np.array(list(map(int, input().split())), dtype=np.float64)
    B: np.ndarray = np.array(list(map(int, input().split())), dtype=np.float64)

    A.sort()
    B.sort()
    if N % 2 == 0:
        front_a: np.ndarray = A[: N // 2].copy()
        back_a: np.ndarray = A[N // 2 :].copy()

        front_b: np.ndarray = B[: N // 2].copy()
        back_b: np.ndarray = B[N // 2 :].copy()
    else:
        front_a: np.ndarray = A[: N // 2].copy()
        back_a: np.ndarray = A[N // 2 + 1 :].copy()

        front_b: np.ndarray = B[: N // 2].copy()
        back_b: np.ndarray = B[N // 2 + 1 :].copy()

    iqr_a: float = np.median(back_a) - np.median(front_a)
    iqr_b: float = np.median(back_b) - np.median(front_b)

    if abs(iqr_a - iqr_b) < 1e-6:
        print("same")
    elif iqr_a < iqr_b:
        print("A")
    else:
        print("B")


if __name__ == "__main__":
    main()
