from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    B: List[int] = list(map(int, input().split()))

    A: List[int] = [1 << 60 for i in range(N)]

    for i, b in enumerate(B):
        A[i] = min(A[i], b)
        A[i + 1] = min(A[i + 1], b)

    print(sum(A))


if __name__ == "__main__":
    main()
