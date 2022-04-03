from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    A.sort(reverse=True)

    answer: int = 0
    cumsum: List[int] = list(itertools.accumulate(A))
    cumsum.insert(0, 0)
    for i in range(N):
        answer += (N - i - 1) * A[i] - (cumsum[N] - cumsum[i + 1])

    print(answer)


if __name__ == "__main__":
    main()
