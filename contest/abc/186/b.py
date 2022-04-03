from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    minimum: int = 10 ** 8
    for a in A:
        minimum = min(minimum, min(a))

    answer: int = 0
    for ai in A:
        for aij in ai:
            answer += aij - minimum

    print(answer)


if __name__ == "__main__":
    main()
