from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    C: List[int] = list(itertools.accumulate(A))

    mod: int = 1000000007
    answer: int = 0
    for i in range(N):
        answer += A[i] * (C[-1] - C[i]) % mod

    print(answer % mod)


if __name__ == "__main__":
    main()
