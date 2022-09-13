from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    mod: int = 1000000007

    if A[0] != 0:
        print(0)
        return

    answer: int = 1
    RGB: List[int] = [-1, -1, -1]

    for i, a in enumerate(A):
        answer *= RGB.count(a - 1)
        try:
            index: int = RGB.index(a - 1)
            RGB[index] = a
        except ValueError:
            print(0)
            return

        answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
