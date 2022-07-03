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
    N, Q, X = map(int, input().split())
    W: List[int] = list(map(int, input().split()))
    K: List[int] = [int(input()) for i in range(Q)]

    S: int = sum(W)
    C: List[int] = [(X // S) * N] * N
    db: List[List[int]] = [[0 for j in range(N)] for i in range(64)]

    X %= S
    V: List[int] = [0] + list(itertools.accumulate(W * 2))
    for i in range(N):
        j: int = bisect.bisect_left(V, X + V[i])
        C[i] += j - i

    for i in range(N):
        db[0][i] = (i + C[i]) % N

    for i in range(1, 64):
        for j in range(N):
            db[i][j] = db[i - 1][db[i - 1][j]]

    for k in K:
        k -= 1
        index: int = 0
        i: int = 0
        while k:
            if k & 1:
                index = db[i][index]
            k >>= 1
            i += 1

        print(C[index])


if __name__ == "__main__":
    main()
