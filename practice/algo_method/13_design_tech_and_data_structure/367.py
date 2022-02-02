from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    left: float = 0
    right: float = M
    while right - left > 0.001:
        mid = (right + left) / 2

        saving: float = N + 1
        for i in range(5):
            saving *= mid
            saving += 1

        if saving > M:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()
