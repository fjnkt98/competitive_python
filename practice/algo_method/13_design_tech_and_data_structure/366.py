from typing import List
import sys
from array import array


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def solve(X: int) -> int:
    left: int = 0
    right: int = X

    while right - left > 1:
        mid: int = (right + left) // 2

        total: int = mid * (mid + 1) // 2

        if total >= X:
            right = mid
        else:
            left = mid

    return right


def main():
    N: int = int(input())
    X: array[int] = array("q", list(map(int, input().split())))

    for x in X:
        print(solve(x))


if __name__ == "__main__":
    main()
