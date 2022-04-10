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

    B: np.ndarray = 50 + 10 * (A - A.mean()) / A.std()
    print(B[0])


if __name__ == "__main__":
    main()
