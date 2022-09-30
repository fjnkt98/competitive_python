from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = sorted([(a, i) for i, a in enumerate(A)])

    print(B[-2][1] + 1)


if __name__ == "__main__":
    main()
