from typing import List, Tuple
import sys
from array import array
import numpy as np

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())

    p0 = np.array([x0, y0])
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    p3 = np.array([x3, y3])


if __name__ == "__main__":
    main()
