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


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    db: List[List[int]] = [[0 for j in range(N)] for i in range(40)]
    for j in range(N):
        db[0][j] = A[j]

    for i in range(1, 40):
        for j in range(N):
            db[i][j] = db[i - 1][j] + db[i - 1][(j + db[i - 1][j]) % N]

    answer: int = 0
    i: int = 0
    while K:
        if K & 1:
            answer += db[i][answer % N]
        K >>= 1
        i += 1

    print(answer)


if __name__ == "__main__":
    main()
