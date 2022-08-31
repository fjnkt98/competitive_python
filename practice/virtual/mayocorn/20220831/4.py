from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N: int = int(input())

    M: int = math.floor(math.sqrt(N))
    answer: int = 2 * sum([N // x for x in range(1, M + 1)]) - M ** 2

    print(answer)


if __name__ == "__main__":
    main()
