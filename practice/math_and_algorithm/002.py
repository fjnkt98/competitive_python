from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A1, A2, A3 = map(int, input().split())
    print(A1 + A2 + A3)


if __name__ == "__main__":
    main()
