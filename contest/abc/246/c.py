from typing import List, Tuple
import sys
import collections
import itertools
import heapq


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K, X = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    A.sort(reverse=True)
    for i in range(N):
        q: int = A[i] // X
        if K < q:
            A[i] -= K * X
            K = 0
            break
        else:
            A[i] -= q * X
            K -= q

    A.sort(reverse=True)
    for i in range(N):
        if K <= 0:
            break
        A[i] = max(0, A[i] - X)
        K -= 1

    print(sum(A))


if __name__ == "__main__":
    main()
