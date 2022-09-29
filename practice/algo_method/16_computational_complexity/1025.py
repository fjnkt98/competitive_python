from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    Q: int = int(input())
    K: List[int] = [int(input()) for i in range(Q)]

    C: List[int] = [0] + list(itertools.accumulate(A))

    for k in K:
        print(C[k])


if __name__ == "__main__":
    main()
