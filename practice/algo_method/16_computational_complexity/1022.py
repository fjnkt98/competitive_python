from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    print(max(A) - min(A))


if __name__ == "__main__":
    main()
