from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    E: List[float] = [0] * N
    E[0] = 3.5
    for i in range(1, N):
        E[i] = (
            max(1, E[i - 1]) / 6
            + max(2, E[i - 1]) / 6
            + max(3, E[i - 1]) / 6
            + max(4, E[i - 1]) / 6
            + max(5, E[i - 1]) / 6
            + max(6, E[i - 1]) / 6
        )

    print(E[N - 1])


if __name__ == "__main__":
    main()
