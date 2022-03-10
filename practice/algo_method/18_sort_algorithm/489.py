from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    X: List[int] = list(map(int, input().split()))

    A.sort()

    for x in X:
        print(A[x])


if __name__ == "__main__":
    main()
