from typing import List
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    print(A * B)


if __name__ == "__main__":
    main()
