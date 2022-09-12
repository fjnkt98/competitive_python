from typing import *
import collections
import itertools
import bisect
import math


def main():
    A, B = map(int, input().split())

    d: float = math.sqrt(A ** 2 + B ** 2)
    print(A / d, B / d)


if __name__ == "__main__":
    main()
