from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    M1, D1 = map(int, input().split())
    M2, D2 = map(int, input().split())

    if M2 == M1 + 1:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
