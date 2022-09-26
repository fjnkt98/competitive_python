from typing import *
import collections
import itertools
import bisect
import math


def main():
    X: int = int(input())

    Y: int = 100
    answer: int = 0
    while Y < X:
        Y = 101 * Y // 100
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
