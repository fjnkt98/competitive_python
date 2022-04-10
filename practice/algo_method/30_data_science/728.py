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

    a: float = 1 / (H.max() - H.min())
    b: float = -a * H.min()

    print(*(H * a + b))


if __name__ == "__main__":
    main()
