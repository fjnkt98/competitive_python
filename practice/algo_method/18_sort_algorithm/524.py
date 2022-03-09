from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def heapify(A: List[int], i: int, N: int):
    child: int = i * 2 + 1
    if child >= N:
        return

    if child + 1 < N and A[child + 1] > A[child]:
        child += 1

    if A[child] <= A[i]:
        return

    A[i], A[child] = A[child], A[i]

    heapify(A, child, N)


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    for i in range(N // 2 - 1, -1, -1):
        heapify(A, i, N)

    for i in range(N - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)

        if i == M:
            print(" ".join(map(str, A)))

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
