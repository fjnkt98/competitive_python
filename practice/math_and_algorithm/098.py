from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def outer_production(a: List[int], b: List[int]) -> int:
    return a[0] * b[1] - a[1] * b[0]


def main():
    N: int = int(input())
    P: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    P.append(P[0])
    p = list(map(int, input().split()))

    cross: int = 0
    for i in range(N):
        a: List[int] = [P[i][0] - p[0], P[i][1] - p[1]]
        b: List[int] = [P[i + 1][0] - p[0], P[i + 1][1] - p[1]]

        if a[1] > b[1]:
            a, b = b, a

        if outer_production(a, b) > 0 and a[1] <= 0 and b[1] > 0:
            cross += 1

    print("INSIDE" if cross % 2 == 1 else "OUTSIDE")


if __name__ == "__main__":
    main()
