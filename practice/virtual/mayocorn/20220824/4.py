from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    C = collections.Counter()
    answer: int = 0
    for j in range(N):
        answer += C[j + 1 - A[j]]
        C[j + 1 + A[j]] += 1

    print(answer)


if __name__ == "__main__":
    main()
