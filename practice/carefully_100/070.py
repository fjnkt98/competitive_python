from typing import *
import collections
import itertools
import bisect
import math


def main():
    M, N = map(int, input().split())
    mod: int = 1000000007
    print(pow(M, N, mod))


if __name__ == "__main__":
    main()
