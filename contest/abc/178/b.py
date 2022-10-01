from typing import *
import collections
import itertools
import bisect
import math


def main():
    a, b, c, d = map(int, input().split())

    answer: int = -(1 << 60)
    for x, y in itertools.product([a, b], [c, d]):
        answer = max(answer, x * y)

    print(answer)


if __name__ == "__main__":
    main()
