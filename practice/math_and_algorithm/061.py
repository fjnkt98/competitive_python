from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    ref: int = 1
    for i in range(64):
        if N == ref - 1:
            print("Second")
            return
        ref *= 2

    print("First")


if __name__ == "__main__":
    main()
