from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(N: int):
    if N == 1:
        return 1
    return N * f(N - 1)


def main():
    N = int(input())
    print(f(N))


if __name__ == "__main__":
    main()
