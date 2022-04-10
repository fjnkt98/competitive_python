from typing import List, Tuple
import sys
import collections
import itertools
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    H: np.ndarray = np.array(list(map(int, input().split())), dtype=np.float64)

    mean: float = H.mean()
    sigma: float = H.std()

    print(*((H - mean) / sigma))


if __name__ == "__main__":
    main()
