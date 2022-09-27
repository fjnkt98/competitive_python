from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    for (x, y), (x1, y1), (x2, y2) in itertools.combinations(zip(X, Y), r=3):
        if (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1):
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
