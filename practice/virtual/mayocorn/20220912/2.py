from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    T, A = map(int, input().split())
    H: List[int] = list(map(int, input().split()))

    B: List[float] = [T - 0.006 * x for x in H]
    D: List[float] = [abs(A - b) for b in B]

    answer: int = 0
    temp: float = 1e9
    for i, d in enumerate(D):
        if d < temp:
            answer = i
            temp = d

    print(answer + 1)


if __name__ == "__main__":
    main()
