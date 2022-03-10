from typing import List, Tuple, Counter
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    vote: Counter[int] = collections.Counter(A)
    rank: List[Tuple[int, int]] = [(0, i) for i in range(N)]
    for i, v in vote.items():
        rank[i] = (-v, i)

    rank.sort()

    for v, i in rank:
        print(f"{i} {-v}")


if __name__ == "__main__":
    main()
