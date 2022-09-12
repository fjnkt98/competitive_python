from typing import *
import collections
import itertools
import bisect
import math


def dist(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    N, M = map(int, input().split())
    A: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for i in range(N)]
    B: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(M)]

    if N == 0:
        answer = 1 << 60
    else:
        answer: int = min([r for x, y, r in A])

    for x1, y1 in B:
        r1: int = 1 << 60
        for x2, y2, r2 in A:
            r1 = min(r1, dist(x1, y1, x2, y2) - r2)

        for x2, y2 in B:
            if (x1, y1) == (x2, y2):
                continue

            r1 = min(r1, dist(x1, y1, x2, y2) / 2)

        answer = min(answer, r1)

    print(answer)


if __name__ == "__main__":
    main()
