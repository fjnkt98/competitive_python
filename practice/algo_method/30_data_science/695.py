from typing import List, Tuple
import sys
import collections
import itertools
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: np.ndarray = np.array(list(map(int, input().split())), dtype=np.int64)

    print(np.median(A))


if __name__ == "__main__":
    main()
