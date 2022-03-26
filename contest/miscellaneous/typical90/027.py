from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
# input = sys.stdin.readline


def main():
    N: int = int(input())
    S: List[str] = [input() for i in range(N)]

    registered: Set[str] = set()
    for i, s in enumerate(S):
        if s not in registered:
            print(i + 1)
            registered.add(s)


if __name__ == "__main__":
    main()
