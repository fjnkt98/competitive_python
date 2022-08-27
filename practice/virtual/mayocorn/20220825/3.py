from typing import *
import collections
import itertools
import bisect
import math


def main():
    X, Y, A, B = map(int, input().split())

    answer: int = 0
    while A * X < Y and A * X <= X + B:
        X *= A
        answer += 1

    answer += (Y - X - 1) // B
    print(answer)


if __name__ == "__main__":
    main()
