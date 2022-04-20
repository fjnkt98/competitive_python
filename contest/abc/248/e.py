from typing import List, Tuple, Set
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def normalize(numerator: int, denominator: int) -> Tuple[int, int]:
    if numerator == 0 and denominator < 0:
        denominator *= -1
    elif numerator < 0:
        numerator *= -1
        denominator *= -1

    gcd: int = math.gcd(abs(numerator), abs(denominator))

    numerator //= gcd
    denominator //= gcd

    return (numerator, denominator)


def parameterize(xi: int, yi: int, xj: int, yj: int) -> Tuple[int, int, int, int]:
    if xi == xj:
        return (xi, 0, 0, 0)
    else:
        slope = normalize(yj - yi, xj - xi)
        intercept = normalize(xj * yi - xi * yj, xj - xi)

        return (*slope, *intercept)


def main():
    N, K = map(int, input().split())
    P: List[Tuple[int]] = [tuple(map(int, input().split())) for i in range(N)]

    if K == 1:
        print("Infinity")
        return

    answer: int = 0
    lines: Set[Tuple[int, int, int, int]] = set()
    for (xi, yi), (xj, yj) in itertools.combinations(P, 2):

        line = parameterize(xi, yi, xj, yj)

        if line in lines:
            continue

        count: int = 2
        for x, y in P:
            if (x, y) == (xi, yi) or (x, y) == (xj, yj):
                continue
            if (y - yi) * (xj - xi) == (yj - yi) * (x - xi):
                count += 1

        if count >= K:
            answer += 1

        lines.add(line)

    print(answer)


if __name__ == "__main__":
    main()
