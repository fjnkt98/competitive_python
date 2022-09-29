from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    D: List[int] = [0] + list(map(int, input().split()))
    Q: int = int(input())
    L, R = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    C: List[int] = list(itertools.accumulate(D))
    for l, r in zip(L, R):
        print(C[r] - C[l])


if __name__ == "__main__":
    main()
