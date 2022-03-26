from typing import List, Tuple
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    T: int = int(input())
    L, X, Y = map(int, input().split())
    Q: int = int(input())
    for i in [0] * Q:
        E: int = int(input())

        angle: float = -2 * math.pi * E / T
        y: float = L * math.sin(angle) / 2
        z: float = L * (1 - math.cos(angle)) / 2

        l: float = math.sqrt(math.pow(X, 2) + math.pow(Y - y, 2))

        print("{:.8f}".format(math.degrees(math.atan2(z, l))))


if __name__ == "__main__":
    main()
