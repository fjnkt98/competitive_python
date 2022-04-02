from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    X: List[int] = [0] * N
    Y: List[int] = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    X.sort()
    Y.sort()

    xp: int = X[N // 2] if N % 2 == 1 else (X[N // 2] + X[N // 2 - 1]) // 2
    yp: int = Y[N // 2] if N % 2 == 1 else (Y[N // 2] + Y[N // 2 - 1]) // 2

    answer: int = 0
    for x, y in zip(X, Y):
        answer += abs(x - xp) + abs(y - yp)

    print(answer)


if __name__ == "__main__":
    main()
