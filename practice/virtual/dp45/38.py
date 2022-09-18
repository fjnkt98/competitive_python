from typing import *
import collections
import itertools
import bisect
import math


import sys

sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())

    mod: int = 1000000007
    memo = [{} for i in range(N + 1)]

    def ok(tail: str) -> bool:
        for i in range(4):
            t = list(tail)
            if i >= 1:
                t[i - 1], t[i] = t[i], t[i - 1]
            if "AGC" in "".join(t):
                return False
        return True

    def dfs(current: int, tail: str) -> int:
        if tail in memo[current]:
            return memo[current][tail]

        if current == N:
            return 1

        count: int = 0
        for c in "ACGT":
            if ok(tail + c):
                count += dfs(current + 1, tail[1:] + c)
                count %= mod
        memo[current][tail] = count
        return count % mod

    answer: int = dfs(0, "TTT")
    print(answer)


if __name__ == "__main__":
    main()
