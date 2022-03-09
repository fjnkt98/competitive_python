from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    for i in range(N - 1):
        j = A[i:].index(min(A[i:])) + i
        A[i], A[j] = A[j], A[i]
        print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
