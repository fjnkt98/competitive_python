from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    T: int = int(input())
    N: int = int(input())
    A: List[int] = [0 for i in range(T + 1)]
    for i in range(N):
        L, R = map(int, input().split())

        A[L] += 1
        A[R] -= 1

    C = list(itertools.accumulate(A))

    for c in C[:-1]:
        print(c)


if __name__ == "__main__":
    main()
