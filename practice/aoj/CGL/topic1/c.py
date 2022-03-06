from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    x0, y0, x1, y1 = map(int, input().split())
    Q = int(input())
    x: List[int] = [0 for i in range(Q)]
    y: List[int] = [0 for i in range(Q)]
    for i in range(Q):
        x[i], y[i] = map(int, input().split())

    p0 = np.array([x0, y0])
    p1 = np.array([x1, y1])

    for x2, y2 in zip(x, y):
        p2 = np.array([x2, y2])

        p01 = p1 - p0
        p02 = p2 - p0

        if np.cross(p01, p02) > 0:
            print("COUNTER_CLOCKWISE")
        elif np.cross(p01, p02) < 0:
            print("CLOCKWISE")
        elif np.dot(p01, p02) < 0:
            print("ONLINE_BACK")
        elif np.linalg.norm(p01) < np.linalg.norm(p02):
            print("ONLINE_FRONT")
        else:
            print("ON_SEGMENT")


if __name__ == "__main__":
    main()
