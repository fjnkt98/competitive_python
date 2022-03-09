from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    X: int = max(A) + 1
    num: List[int] = [0 for i in range(X)]
    for a in A:
        num[a] += 1

    acc: List[int] = [0 for i in range(X)]
    for i in range(X):
        if i == 0:
            acc[i] = num[i]
        else:
            acc[i] = acc[i - 1] + num[i]

    B: List[int] = [0 for i in range(N)]
    for i in range(N):
        acc[A[i]] -= 1
        B[acc[A[i]]] = A[i]

    print(*B)


if __name__ == "__main__":
    main()
