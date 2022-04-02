from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = [int(input()) for i in range(N)]

    print("second" if all(a % 2 == 0 for a in A) else "first")


if __name__ == "__main__":
    main()
