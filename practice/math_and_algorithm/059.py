from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    if N % 4 == 1:
        print(2)
    elif N % 4 == 2:
        print(4)
    elif N % 4 == 3:
        print(8)
    elif N % 4 == 0:
        print(6)


if __name__ == "__main__":
    main()
