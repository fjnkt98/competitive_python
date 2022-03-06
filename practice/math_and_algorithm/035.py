from typing import List, Tuple
import sys
from array import array
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())

    d: float = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if r1 < r2:
        r1, r2 = r2, r1

    if abs(r1 + r2 - d) < 1e-6:
        print(4)
    elif r1 + r2 < d:
        print(5)
    elif abs(r1 - (r2 + d)) < 1e-6:
        print(2)
    elif r1 > r2 + d:
        print(1)
    else:
        print(3)


if __name__ == "__main__":
    main()
