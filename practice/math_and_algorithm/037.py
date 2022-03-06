from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    p3 = np.array([x3, y3])
    p4 = np.array([x4, y4])

    p12 = p2 - p1
    p13 = p3 - p1
    p14 = p4 - p1

    p31 = p1 - p3
    p32 = p2 - p3
    p34 = p4 - p3

    cross1: int = np.cross(p12, p13)
    cross2: int = np.cross(p12, p14)
    cross3: int = np.cross(p34, p31)
    cross4: int = np.cross(p34, p32)

    if cross1 == 0 and cross2 == 0 and cross3 == 0 and cross4 == 0:
        A = (x1, y1)
        B = (x2, y2)
        C = (x3, y3)
        D = (x4, y4)
        if A > B:
            tmp = B
            B = A
            A = tmp
        if C > D:
            tmp = D
            D = C
            C = tmp

        if max(A, C) <= min(B, D):
            print("Yes")
        else:
            print("No")
    else:
        if ((cross1 >= 0 and cross2 <= 0) or (cross1 <= 0 and cross2 >= 0)) and (
            (cross3 >= 0 and cross4 <= 0) or (cross3 <= 0 and cross4 >= 0)
        ):
            print("Yes")

        else:
            print("No")


if __name__ == "__main__":
    main()
