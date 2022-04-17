from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, K = map(int, input().split())

    answer: int = 0
    while A < B:
        A *= K
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
