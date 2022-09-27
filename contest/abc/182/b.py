from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    answer: int = 0
    count: int = 0
    for k in range(2, 1001):
        c: int = 0
        for a in A:
            if a % k == 0:
                c += 1

        if count < c:
            count = c
            answer = k

    print(answer)


if __name__ == "__main__":
    main()
