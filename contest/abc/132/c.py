from typing import List, Tuple
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    D: List[int] = list(map(int, input().split()))

    D.sort()

    answer: int = D[N // 2] - D[N // 2 - 1]

    print(answer)


if __name__ == "__main__":
    main()
