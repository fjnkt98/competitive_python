from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    if N % 4 == 0:
        print("Second")
    else:
        print("First")


if __name__ == "__main__":
    main()
