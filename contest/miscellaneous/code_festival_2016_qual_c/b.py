from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    K, T = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    print(max(max(A) - (K - max(A)) - 1, 0))


if __name__ == "__main__":
    main()
