from typing import List, Tuple
import sys
import collections
import itertools
import operator


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = [0] * N
    B: List[int] = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    C: List[int] = [2 * a + b for a, b in zip(A, B)]
    X: int = -sum(A)
    C.sort()

    answer: int = 0
    while X <= 0:
        X += C.pop()
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
