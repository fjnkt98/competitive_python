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
import random
import numpy as np

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H1, W1 = map(int, input().split())
    A = np.array([list(map(int, input().split())) for i in range(H1)], dtype=np.int64)
    H2, W2 = map(int, input().split())
    B = np.array([list(map(int, input().split())) for i in range(H2)], dtype=np.int64)

    ok: bool = False
    for rows in itertools.combinations(range(H1), r=H2):
        for cols in itertools.combinations(range(W1), r=W2):
            if np.array_equal(A[rows, :][:, cols], B):
                ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
