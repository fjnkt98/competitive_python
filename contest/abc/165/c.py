from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M, Q = map(int, input().split())
    R: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    answer: int = 0
    for A in itertools.combinations_with_replacement(range(1, M + 1), r=N):
        result: int = 0
        for a, b, c, d in R:
            if A[b - 1] - A[a - 1] == c:
                result += d

        answer = max(answer, result)

    print(answer)


if __name__ == "__main__":
    main()
