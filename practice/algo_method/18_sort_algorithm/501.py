from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    A.sort()

    if N % 2 == 0:
        print((A[N // 2 - 1] + A[N // 2]) / 2)
    else:
        print(A[N // 2])


if __name__ == "__main__":
    main()
