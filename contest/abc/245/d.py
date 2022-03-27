from typing import List, Tuple
import sys
import collections
import itertools
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    C: List[int] = list(map(int, input().split()))

    X: np.ndarray = np.array(list(reversed(A)))
    Z: np.ndarray = np.array(list(reversed(C)))

    Y, _ = np.polydiv(Z, X)
    print(*reversed(list(map(int, Y.tolist()))))


if __name__ == "__main__":
    main()
