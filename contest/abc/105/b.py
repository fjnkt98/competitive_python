from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    for i in range(100):
        for j in range(100):
            if 4 * i + 7 * j == N:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
