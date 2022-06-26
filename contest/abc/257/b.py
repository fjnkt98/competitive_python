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
    N, K, Q = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    L: List[int] = list(map(int, input().split()))

    board: List[int] = [0 for i in range(N)]
    A = [a - 1 for a in A]
    for a in A:
        board[a] = 1

    for i in [l - 1 for l in L]:
        if A[i] == N - 1:
            continue
        if board[A[i] + 1] == 0:
            board[A[i]] = 0
            board[A[i] + 1] = 1
            A[i] += 1
        else:
            continue

    answer: List[int] = []
    for i, b in enumerate(board):
        if b == 1:
            answer.append(i + 1)

    print(*answer)


if __name__ == "__main__":
    main()
