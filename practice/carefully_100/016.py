from math import perm
from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    P: List[int] = list(map(int, input().split()))
    Q: List[int] = list(map(int, input().split()))

    permutations: List[Tuple] = []
    for p in itertools.permutations(range(1, N + 1)):
        permutations.append(tuple(p))

    permutations.sort()
    x: int = 0
    y: int = 0
    for i, p in enumerate(permutations):
        if p == tuple(P):
            x = i
        if p == tuple(Q):
            y = i

    print(abs(x - y))


if __name__ == "__main__":
    main()
