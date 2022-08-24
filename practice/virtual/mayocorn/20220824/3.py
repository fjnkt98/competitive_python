from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, X, Y = map(int, input().split())

    red: List[int] = [0 for i in range(N + 1)]
    blue: List[int] = [0 for i in range(N + 1)]

    red[N] = 1
    for i in range(N, 1, -1):
        red[i - 1] += red[i]
        blue[i] += X * red[i]

        red[i - 1] += blue[i]
        blue[i - 1] += Y * blue[i]

    print(blue[1])


if __name__ == "__main__":
    main()
