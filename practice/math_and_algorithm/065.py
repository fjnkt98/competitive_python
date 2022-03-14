from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())

    if H == 1 or W == 1:
        print(1)
    elif (H * W) % 2 == 0:
        print(H * W // 2)
    else:
        print(H * W // 2 + 1)


if __name__ == "__main__":
    main()
