from typing import *
import collections
import itertools
import bisect
import math


def main():
    K, S = map(int, input().split())

    answer: int = 0
    for X, Y in itertools.product(range(K + 1), repeat=2):
        Z: int = S - X - Y

        if not 0 <= Z <= K:
            continue

        if X + Y + Z == S:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
