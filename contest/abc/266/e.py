from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    answer: int = 3.5
    for i in range(1, N):
        E: float = 0.0
        for j in range(1, 7):
            E += max(answer, j) / 6
        answer = E

    print(answer)


if __name__ == "__main__":
    main()
