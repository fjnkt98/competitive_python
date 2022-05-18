from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def compress(A: List[int]) -> List[int]:
    X: List[int] = sorted(set(A))
    D: Dict[int, int] = {x: i for i, x in enumerate(X)}
    return list(map(lambda x: D[x], A))


def main():
    N: int = int(input())
    A: List[int] = [int(input()) for i in range(N)]

    for a in compress(A):
        print(a)


if __name__ == "__main__":
    main()
