from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    Q = int(input())
    query: List[List[int]] = [[] for i in range(Q)]
    for i in range(Q):
        query[i] = list(map(int, input().split()))

    for q in query:
        x1, y1, x2, y2, x3, y3, x4, y4 = q

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

        if (
            np.cross(p12, p13) == 0
            and np.cross(p12, p14) == 0
            and np.cross(p34, p32) == 0
            and np.cross(p34, p31) == 0
        ):
            A = (x1, y1)
            B = (x2, y2)
            C = (x3, y3)
            D = (x4, y4)
            if A > B:
                A, B = B, A
            if C > D:
                C, D = D, C

            if max(A, C) <= min(B, D):
                print("Yes")
            else:
                print("No")
        else:
            if (
                np.cross(p12, p13) * np.cross(p12, p14) <= 0
                and np.cross(p34, p32) * np.cross(p34, p31) <= 0
            ):
                print("Yes")

            else:
                print("No")


if __name__ == "__main__":
    main()
