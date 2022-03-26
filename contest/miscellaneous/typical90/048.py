from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = [0] * N
    B: List[int] = [0] * N
    P: List[int] = [0] * (2 * N)
    for i in range(N):
        A[i], B[i] = map(int, input().split())
        P[2 * i] = B[i]
        P[2 * i + 1] = A[i] - B[i]

    P.sort(reverse=True)

    answer: int = 0
    for i in range(K):
        answer += P[i]

    print(answer)


if __name__ == "__main__":
    main()
