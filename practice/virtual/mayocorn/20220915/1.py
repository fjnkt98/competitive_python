from typing import *
import collections
import itertools
import bisect
import math


def main():
    S, T = map(int, input().split())

    answer: int = 0
    for (
        a,
        b,
        c,
    ) in itertools.product(range(101), repeat=3):
        if a + b + c <= S and a * b * c <= T:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
