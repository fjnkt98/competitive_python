from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    C: List[int] = list(itertools.accumulate(A))

    for k in range(1, N + 1):
        answer: int = sum(A[:k])
        for i in range(N - k):
            answer = max(answer, C[i + k] - C[i])
        print(answer)


if __name__ == "__main__":
    main()
