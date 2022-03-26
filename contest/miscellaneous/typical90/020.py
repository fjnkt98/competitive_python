from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    if a < pow(c, b):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
