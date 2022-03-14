from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    print("Yes" if N % 2 == 0 else "No")


if __name__ == "__main__":
    main()
