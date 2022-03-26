from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    A.sort()
    B.sort()

    answer: int = 0
    for a, b in zip(A, B):
        answer += abs(a - b)

    print(answer)


if __name__ == "__main__":
    main()
