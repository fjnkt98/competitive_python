from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())

    if H == 1 or W == 1:
        print(H * W)
    else:
        print(((H + 1) // 2) * ((W + 1) // 2))


if __name__ == "__main__":
    main()
