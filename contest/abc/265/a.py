from typing import *
import collections
import itertools
import bisect
import math


def main():
    X, Y, N = map(int, input().split())

    answer: int = 0
    if N < 3:
        while N > 0:
            N -= 1
            answer += X

        print(answer)
    elif 3 * X > Y:
        while N >= 3:
            N -= 3
            answer += Y

        while N > 0:
            N -= 1
            answer += X

        print(answer)

    else:
        while N > 0:
            N -= 1
            answer += X

        print(answer)


if __name__ == "__main__":
    main()
