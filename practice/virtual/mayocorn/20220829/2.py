from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    C: List[int] = sorted(list(map(int, input().split())))

    mod: int = 1000000007
    answer: int = C[0]
    for i, c in enumerate(C):
        if i == 0:
            continue
        answer *= c - i
        answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
