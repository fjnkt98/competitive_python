from typing import List, Tuple
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = sorted(list(map(int, input().split())))
    Q: int = int(input())
    B: List[int] = [int(input()) for i in range(Q)]

    A.append(1 << 60)

    for b in B:
        index: int = bisect.bisect_left(A, b)
        diff: int = min(abs(A[index] - b), abs(A[index - 1] - b))
        print(diff)


if __name__ == "__main__":
    main()
