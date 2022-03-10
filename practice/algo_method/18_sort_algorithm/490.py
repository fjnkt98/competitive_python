from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    A.sort()

    answer: int = 1 << 60
    head: int = 0
    tail: int = 0
    for i in range(N - K + 1):
        answer = min(answer, A[i + K - 1] - A[i])

    print(answer)


if __name__ == "__main__":
    main()
