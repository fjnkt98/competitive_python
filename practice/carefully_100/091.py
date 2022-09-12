from typing import *
import collections
import itertools
import bisect
import math


def main():
    A, B, C = map(int, input().split())

    if (A ** 2) * B == 2 * C:
        answer: float = math.atan2(A, B)
        print(math.degrees(answer))
    elif (A ** 2) * B < 2 * C:
        x: float = (2 * C) / (A ** 2) - B
        answer: float = math.atan2(B - x, A)
        print(math.degrees(answer))
    else:
        x: float = (2 * C) / (A * B)
        answer: float = math.atan2(B, x)
        print(math.degrees(answer))


if __name__ == "__main__":
    main()
