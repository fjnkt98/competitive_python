from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    X: int = int(input())

    C: int = X // 100

    if 100 * C <= X <= 105 * C:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
