from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    if x1 == x2:
        x: int = x3
    elif x2 == x3:
        x: int = x1
    else:
        x: int = x2

    if y1 == y2:
        y: int = y3
    elif y2 == y3:
        y: int = y1
    else:
        y: int = y2

    print(x, y)


if __name__ == "__main__":
    main()
