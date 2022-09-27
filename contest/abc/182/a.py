from typing import *
import collections
import itertools
import bisect
import math


def main():
    A, B = map(int, input().split())

    print(max(0, 2 * A + 100 - B))


if __name__ == "__main__":
    main()
