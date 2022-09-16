from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    A: List[int] = sorted(map(int, input().split()))
    B: List[int] = sorted(map(int, input().split()))

    answer: int = 1 << 60
    for i, a in enumerate(A):
        j: int = bisect.bisect_left(B, a)
        answer = min(answer, abs(a - B[min(M - 1, j - 1)]), abs(a - B[min(M - 1, j)]))

    print(answer)


if __name__ == "__main__":
    main()
