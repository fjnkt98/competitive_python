from typing import List, Tuple
import sys
import collections
import itertools
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: np.ndarray = np.array(list(map(int, input().split())), dtype=np.int64)

    print(*(A * K))


if __name__ == "__main__":
    main()
