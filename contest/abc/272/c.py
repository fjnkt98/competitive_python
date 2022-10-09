from typing import *
import collections
import itertools
import bisect
import math
import random


def solve(N: int, A: List[int]) -> int:
    A.sort(reverse=True)
    evens: List[int] = []
    odds: List[int] = []
    for a in A:
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)

    answer: int = -1
    if len(evens) >= 2:
        answer = max(answer, evens[0] + evens[1])
    if len(odds) >= 2:
        answer = max(answer, odds[0] + odds[1])

    return answer


def naive(N: int, A: List[int]) -> int:
    answer: int = -1
    for ai, aj in itertools.combinations(A, r=2):
        if (ai + aj) % 2 == 0:
            answer = max(answer, ai + aj)

    return answer


def main():
    N: int = int(input())
    A: List[int] = sorted(list(map(int, input().split())), reverse=True)
    print(solve(N, A))


if __name__ == "__main__":
    main()
