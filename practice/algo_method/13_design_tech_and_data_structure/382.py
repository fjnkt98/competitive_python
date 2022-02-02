from typing import List
import sys
import bisect


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    A.sort()

    for b in B:
        print(bisect.bisect_right(A, b))


if __name__ == "__main__":
    main()
