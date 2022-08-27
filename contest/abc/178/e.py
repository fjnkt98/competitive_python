from typing import *
import collections
import itertools
import bisect
import math


def solve(N: int, X: List[int], Y: List[int]) -> int:
    Xr, Yr = map(list, zip(*[(x - y, x + y) for x, y in zip(X, Y)]))

    x_min: int = min(Xr)
    x_max: int = max(Xr)
    y_min: int = min(Yr)
    y_max: int = max(Yr)

    answer: int = 0
    for x, y in zip(Xr, Yr):
        answer = max(
            answer, max(abs(x - x_min), abs(x - x_max), abs(y - y_min), abs(y - y_max))
        )

    return answer


def naive(N: int, X: List[int], Y: List[int]) -> int:
    answer: int = 0
    for (xi, yi), (xj, yj) in itertools.combinations(zip(X, Y), r=2):
        answer = max(answer, abs(xi - xj) + abs(yi - yj))

    return answer


def main():
    N: int = int(input())
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    print(solve(N, X, Y))


if __name__ == "__main__":
    main()
