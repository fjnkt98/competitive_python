from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    print(2 * N + 3)


if __name__ == "__main__":
    main()
