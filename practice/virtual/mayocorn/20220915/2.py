from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    C: List[int] = [0] * N
    for i, a in enumerate(A):
        count: int = 0
        while a % 2 == 0:
            count += 1
            a //= 2

        C[i] = count

    print(sum(C))


if __name__ == "__main__":
    main()
