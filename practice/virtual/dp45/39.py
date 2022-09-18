from typing import *
import collections
import itertools
import bisect
import math
import sys

sys.setrecursionlimit(1000000)


memo: Dict[Tuple[int, int, int], float] = {}


def f(x: int, y: int, z: int) -> float:
    if x == 100 or y == 100 or z == 100:
        return 0.0

    if (x, y, z) in memo:
        return memo[(x, y, z)]

    result: float = (
        x * (f(x + 1, y, z) + 1) + y * (f(x, y + 1, z) + 1) + z * (f(x, y, z + 1) + 1)
    ) / (x + y + z)
    memo[(x, y, z)] = result
    return result


def main():
    A, B, C = map(int, input().split())

    print(f(A, B, C))


if __name__ == "__main__":
    main()
