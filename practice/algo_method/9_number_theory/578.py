from typing import List, Tuple
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def factorize(N: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []

    i: int = 2
    while i * i <= N:
        if N % i == 0:
            exp: int = 0

            while N % i == 0:
                N //= i
                exp += 1

            result.append((i, exp))
        i += 1

    if N != 1:
        result.append((N, 1))

    return result


def main():
    N, M = map(int, input().split())
    answer: int = 1
    for p, exp in factorize(M):
        m: int = exp // N
        answer *= m + 1

    print(answer)


if __name__ == "__main__":
    main()
