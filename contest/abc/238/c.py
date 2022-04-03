from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(x: int) -> int:
    return x * (x + 1) // 2


def main():
    N: int = int(input())
    mod: int = 998244353

    digit: int = len(str(N))
    answer: int = 0
    for i in range(1, digit + 1):
        answer += f(min(N, 10 ** i - 1) - (10 ** (i - 1) - 1))
        answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
