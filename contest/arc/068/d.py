from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    counter = collections.Counter(A)
    if len(counter) % 2 == 0:
        print(len(counter) - 1)
    else:
        print(len(counter))


if __name__ == "__main__":
    main()
