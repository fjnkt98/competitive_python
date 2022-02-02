from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N = int(input())

    right: float = 101.0
    left: float = 0.0

    while right - left > 0.001:
        mid: float = (right + left) / 2

        if mid * (mid * (mid + 1) + 2) + 3 < N:
            left = mid
        else:
            right = mid

    print(right)


if __name__ == "__main__":
    main()
