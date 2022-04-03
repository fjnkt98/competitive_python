from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, W = map(int, input().split())

    print(N // W)


if __name__ == "__main__":
    main()
