from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    P: List[int] = list(map(int, input().split()))

    Q: List[int] = [-1] * N
    for i, p in enumerate(P):
        Q[p - 1] = i + 1

    print(*Q)


if __name__ == "__main__":
    main()
