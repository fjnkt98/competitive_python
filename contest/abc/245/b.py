from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    available: Set[int] = set(range(2001))
    available = available - set(A)

    print(sorted(list(available))[0])


if __name__ == "__main__":
    main()
