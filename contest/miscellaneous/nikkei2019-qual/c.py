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

    P: List[Tuple[int]] = [(a, b, a + b) for a, b in zip(A, B)]
    P.sort(key=operator.itemgetter(2), reverse=True)

    X: int = -sum(B)
    for i, p in enumerate(P):
        a, b, x = p
        if i % 2 == 0:
            X += x

    print(X)


if __name__ == "__main__":
    main()
