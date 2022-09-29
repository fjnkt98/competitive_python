from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    C = list(itertools.accumulate(A))

    answer: int = 0
    for i, a in enumerate(A):
        answer += a * (C[N - 1] - C[i])

    print(answer)


if __name__ == "__main__":
    main()
