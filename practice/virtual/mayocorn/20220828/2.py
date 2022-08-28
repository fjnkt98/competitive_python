from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    S: List[str] = [input() for i in range(N)]
    M: int = int(input())
    T: List[str] = [input() for i in range(M)]

    CS = collections.Counter(S)
    CT = collections.Counter(T)

    answer: int = 0
    for s in set(S):
        answer = max(answer, CS[s] - CT[s])

    print(answer)


if __name__ == "__main__":
    main()
