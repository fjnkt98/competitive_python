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
    A.sort()
    if N % 2 == 0:
        front: np.ndarray = A[: N // 2].copy()
        back: np.ndarray = A[N // 2 :].copy()
    else:
        front: np.ndarray = A[: N // 2].copy()
        back: np.ndarray = A[N // 2 + 1 :].copy()

    print(np.median(front), np.median(A), np.median(back))


if __name__ == "__main__":
    main()
