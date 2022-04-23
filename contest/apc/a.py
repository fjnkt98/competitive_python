from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    X, Y = map(int, input().split())

    if X % Y == 0:
        print(-1)
    else:
        print(X)


if __name__ == "__main__":
    main()
