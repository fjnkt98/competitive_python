from typing import List, Tuple
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def divisors(N: int) -> List[int]:
    result: List[int] = []

    i: int = 1
    while i * i <= N:
        if N % i == 0:
            result.append(i)

            if N // i != i:
                result.append(N // i)
        i += 1

    return sorted(result)


def main():
    N, M = map(int, input().split())

    D: List[int] = divisors(M)

    if N > M:
        print(0)
        return

    answer: int = 0
    for d in D:
        if N * d <= M:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
