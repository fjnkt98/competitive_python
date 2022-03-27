from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, C, D = map(int, input().split())

    if A * 3600 + B * 60 < C * 3600 + D * 60 + 1:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
