from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


mod: int = 1000000007


def count(x: int) -> int:
    return ((x // 2) * (x + 1)) % mod if x % 2 == 0 else (((x + 1) // 2) * x) % mod


def main():
    L, R = map(int, input().split())

    pow10: List[int] = [10 ** i for i in range(20)]

    answer: int = 0
    for i in range(1, 20):
        left: int = max(L, pow10[i - 1])
        right: int = min(R, pow10[i] - 1)

        if left > right:
            continue

        answer += i * (count(right) - count(left - 1))
        answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
