from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    X, u, sigma = map(int, input().split())
    print(50 + 10 * (X - u) / sigma)


if __name__ == "__main__":
    main()
