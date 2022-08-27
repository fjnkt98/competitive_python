from typing import *
import collections
import itertools
import bisect
import math


def main():
    x1, y1, x2, y2 = map(int, input().split())

    a: List[int] = [x2 - x1, y2 - y1]
    b: List[int] = [y1 - y2, x2 - x1]

    x3: int = x2 + b[0]
    y3: int = y2 + b[1]

    x4: int = x3 - a[0]
    y4: int = y3 - a[1]

    print(x3, y3, x4, y4)


if __name__ == "__main__":
    main()
