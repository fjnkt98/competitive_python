from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    S: str = input().rstrip()

    x: int = 0
    y: int = 0
    d: int = 0
    dx: List[int] = [1, 0, -1, 0]
    dy: List[int] = [0, -1, 0, 1]
    for s in S:
        if s == "S":
            x += dx[d]
            y += dy[d]
        if s == "R":
            d += 1
            d %= 4

    print(x, y)


if __name__ == "__main__":
    main()
