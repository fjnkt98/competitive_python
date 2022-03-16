from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    A.sort(reverse=True)
    cumsum: List[int] = list(itertools.accumulate(A))

    answer: int = 0
    for i in range(N):
        answer += (N - i - 1) * A[i] - (cumsum[-1] - cumsum[i])

    print(answer)


if __name__ == "__main__":
    main()
