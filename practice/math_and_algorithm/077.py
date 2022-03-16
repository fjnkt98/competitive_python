from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    X: List[int] = [0 for i in range(N)]
    Y: List[int] = [0 for i in range(N)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    X.sort(reverse=True)
    Y.sort(reverse=True)
    CX = list(itertools.accumulate(X))
    CY = list(itertools.accumulate(Y))

    answer: int = 0
    for i in range(N):
        answer += (N - i - 1) * X[i] - (CX[-1] - CX[i])
        answer += (N - i - 1) * Y[i] - (CY[-1] - CY[i])

    print(answer)


if __name__ == "__main__":
    main()
