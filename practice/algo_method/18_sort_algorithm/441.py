from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    for i in range(1, N):
        position: int = i
        while position != 0 and A[position - 1] > A[position]:
            A[position - 1], A[position] = A[position], A[position - 1]
            position -= 1

        print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
