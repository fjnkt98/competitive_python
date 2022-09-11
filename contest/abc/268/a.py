from typing import *
import collections
import itertools
import bisect
import math


def main():
    A: List[int] = list(map(int, input().split()))
    print(len(set(A)))


if __name__ == "__main__":
    main()
