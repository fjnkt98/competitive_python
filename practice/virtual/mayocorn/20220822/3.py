from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N: int = int(input())
    A: List[int] = sorted(list(map(int, input().split())))

    B: List[int] = sorted(A * 2, reverse=True)
    print(sum(B[1:N]))


if __name__ == "__main__":
    main()
