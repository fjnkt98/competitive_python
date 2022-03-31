from typing import List, Tuple
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(x: int) -> int:
    y: int = sum(map(lambda s: ord(s) - ord("0"), str(x)))
    return (x + y) % 100000


def main():
    N, K = map(int, input().split())

    M: int = math.ceil(math.log2(K))

    db: List[List[int]] = [[0 for j in range(100000)] for i in range(M + 1)]

    for j in range(100000):
        db[0][j] = f(j)

    for i in range(1, M + 1):
        for j in range(100000):
            db[i][j] = db[i - 1][db[i - 1][j]]

    answer: int = N
    for i in range(M + 1):
        if K & (1 << i):
            answer = db[i][answer]

    print(answer)


if __name__ == "__main__":
    main()
