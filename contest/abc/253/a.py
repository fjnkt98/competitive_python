from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    A = sorted([a, b, c])

    if b == A[1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
