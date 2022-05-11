from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())

    color: List[List[int]] = [
        [0 if (i + j) % 2 == 0 else 1 for j in range(N)] for i in range(N)
    ]
    grid: List[List[str]] = [
        ["." if color[i // A][j // B] == 0 else "#" for j in range(B * N)]
        for i in range(A * N)
    ]

    for g in grid:
        print(*g, sep="")


if __name__ == "__main__":
    main()
