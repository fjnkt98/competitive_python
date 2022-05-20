from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    V, T, S, D = map(int, input().split())

    if V * T <= D <= V * S:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
