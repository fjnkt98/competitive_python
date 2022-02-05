from typing import List
import sys
from array import array
import math


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    L: array[int] = array("q", list(map(int, input().split())))

    left: float = 0
    right: float = max(L)

    while right - left > 1e-7:
        mid: float = (right + left) / 2

        strings: int = 0
        for line in L:
            strings += math.trunc(line / mid)

        if strings < K:
            right = mid
        else:
            left = mid

    print("{:.6f}".format(left))


if __name__ == "__main__":
    main()
