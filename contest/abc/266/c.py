from typing import *
import collections
import itertools
import bisect
import math


def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())

    a: List[int] = [bx - ax, by - ay]
    b: List[int] = [cx - bx, cy - by]
    c: List[int] = [dx - cx, dy - cy]
    d: List[int] = [ax - dx, ay - dy]

    A: int = a[0] * b[1] - a[1] * b[0]
    B: int = b[0] * c[1] - b[1] * c[0]
    C: int = c[0] * d[1] - c[1] * d[0]
    D: int = d[0] * a[1] - d[1] * a[0]

    if any(map(lambda x: x < 0, [A, B, C, D])):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
