from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    S: List[int] = [int(input()) for i in range(N - 1)]
    A: List[int] = [int(input()) for i in range(M)]

    C: List[int] = [0] + list(itertools.accumulate(S))
    answer: int = 0
    current: int = 0
    for a in A:
        if a > 0:
            i: int = current
            j: int = current + a
        else:
            i: int = current + a
            j: int = current

        answer += C[j] - C[i]

        current += a

    print(answer % 100000)


if __name__ == "__main__":
    main()
