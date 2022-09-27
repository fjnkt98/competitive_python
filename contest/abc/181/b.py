from typing import *
import collections
import itertools
import bisect
import math


def f(A: int, B: int) -> int:
    return (B - A + 1) * (A + B) // 2


def main():
    N: int = int(input())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    answer: int = 0
    for a, b in zip(A, B):
        answer += f(a, b)

    print(answer)


if __name__ == "__main__":
    main()
