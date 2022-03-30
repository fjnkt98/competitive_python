from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, L = map(int, input().split())
    K: int = int(input())
    A: List[int] = list(map(int, input().split()))

    left: int = 0
    right: int = L + 1

    while right - left > 1:
        mid: int = (right + left) // 2

        split_count: int = 0
        last_split: int = 0

        for a in A:
            if a - last_split >= mid and L - a >= mid:
                split_count += 1
                last_split = a

        if split_count >= K:
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
