from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    B: List[int] = []
    current: int = A[0]
    chain: int = 1
    for i in range(1, N):
        if A[i] != current:
            chain += 1
        else:
            B.append(chain)
            chain = 1

        current = A[i]

    B.append(chain)

    if len(B) <= 3:
        print(sum(B))
    else:
        answer: int = 0
        for i in range(len(B) - 2):
            answer = max(answer, B[i] + B[i + 1] + B[i + 2])

        print(answer)


if __name__ == "__main__":
    main()
