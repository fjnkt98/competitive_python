from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())

    answer: int = 0
    for x, y in itertools.product(range(1, N + 1), repeat=2):
        if M - x - y >= 1:
            answer += min(N, M - x - y)

    print(answer)


if __name__ == "__main__":
    main()
