from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A: str = input().rstrip()
    B: str = input().rstrip()

    if len(A) > len(B):
        print(A)
    else:
        print(B)


if __name__ == "__main__":
    main()
