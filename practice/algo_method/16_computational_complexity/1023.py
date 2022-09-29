from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    S: int = sum(A)
    answer: int = 0
    for a in A:
        answer = max(answer, S - a)

    print(answer)


if __name__ == "__main__":
    main()
