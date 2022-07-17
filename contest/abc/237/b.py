from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    B = np.array(A).T.tolist()
    for b in B:
        print(*b)


if __name__ == "__main__":
    main()
