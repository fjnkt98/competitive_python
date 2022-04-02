from typing import List, Tuple
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    D: float = math.sqrt(A ** 2 + B ** 2)
    x: float = A / D
    y: float = B / D
    print("{:.8f} {:.8f}".format(x, y))


if __name__ == "__main__":
    main()
