from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    answer: float = 0.0
    for i in range(N):
        answer += A[i] / 3 + 2 * B[i] / 3

    print(answer)


if __name__ == "__main__":
    main()
