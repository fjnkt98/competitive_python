from typing import List, Tuple
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    Q: int = int(input())
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    index: List[List[int]] = [[] for i in range(N + 1)]

    for i, a in enumerate(A):
        index[a].append(i)

    for i in range(N):
        index[i].sort()

    for l, r, x in query:
        left: int = bisect.bisect_left(index[x], l - 1)
        right: int = bisect.bisect_right(index[x], r - 1)
        print(right - left)


if __name__ == "__main__":
    main()
