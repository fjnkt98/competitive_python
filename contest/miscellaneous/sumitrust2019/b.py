from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    for X in range(1, 50000):
        if N == math.floor(X * 108 // 100):
            print(X)
            return

    print(":(")


if __name__ == "__main__":
    main()
