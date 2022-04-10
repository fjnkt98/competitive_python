from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    u, sigma, a0, a1 = map(int, input().split())

    print(a1 * u + a0, a1 * sigma)


if __name__ == "__main__":
    main()
