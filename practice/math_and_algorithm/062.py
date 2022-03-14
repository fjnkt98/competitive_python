from typing import List, Tuple, DefaultDict
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    A = list(map(lambda x: x - 1, A))

    db: List[List[int]] = [[0 for j in range(N)] for i in range(61)]
    for j in range(N):
        db[0][j] = A[j]

    for i in range(1, 61):
        for j in range(N):
            db[i][j] = db[i - 1][db[i - 1][j]]

    answer: int = 0
    for i in range(61):
        if K & (1 << i):
            answer = db[i][answer]

    print(answer + 1)


if __name__ == "__main__":
    main()
