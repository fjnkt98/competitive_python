from typing import *
import collections
import itertools
import bisect
import math


def main():
    A, B, N = map(int, input().split())

    def f(x: int) -> int:
        return (A * x // B) - A * (x // B)

    answer: int = f(N)
    if B - 1 <= N:
        answer = max(answer, f(B - 1))

    print(answer)


if __name__ == "__main__":
    main()
