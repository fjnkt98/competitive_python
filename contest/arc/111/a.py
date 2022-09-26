from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    print((pow(10, N, M * M) // M) % M)


if __name__ == "__main__":
    main()
