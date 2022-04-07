from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(n: int) -> int:
    if n % 2 == 0:
        if (n // 2) % 2 == 0:
            return n ^ 0
        else:
            return n ^ 1
    else:
        if ((n + 1) // 2) % 2 == 0:
            return 0
        else:
            return 1


def main():
    A, B = map(int, input().split())

    print(f(B) ^ f(A - 1))


if __name__ == "__main__":
    main()
