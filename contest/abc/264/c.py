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

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H1, W1 = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H1)]
    H2, W2 = map(int, input().split())
    B: List[List[int]] = [list(map(int, input().split())) for i in range(H2)]

    ok: bool = False
    for rows in itertools.combinations(range(H1), r=H2):
        for cols in itertools.combinations(range(W1), r=W2):
            C: List[List[int]] = [[0] * W2 for _ in range(H2)]

            for i, row in enumerate(rows):
                for j, col in enumerate(cols):
                    C[i][j] = A[row][col]

            if tuple(itertools.chain(*C)) == tuple(itertools.chain(*B)):
                ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
