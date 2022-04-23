from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, C, D, E, F, X = map(int, input().split())

    takahashi: int = 0
    aoki: int = 0

    for i in range(X):
        if i % (A + C) < A:
            takahashi += B

        if i % (D + F) < D:
            aoki += E

    if takahashi == aoki:
        print("Draw")
    elif takahashi > aoki:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
