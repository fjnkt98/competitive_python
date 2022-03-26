from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    mod: int = 1000000007

    if K == 1:
        print(1 if N == 1 else 0)
        return

    if N == 1:
        print(K)
    else:
        answer: int = (K * (K - 1)) % mod
        answer *= pow(K - 2, N - 2, mod)
        answer %= mod
        print(answer)


if __name__ == "__main__":
    main()
