from typing import List
import sys
from array import array
import bisect


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    answer: int = 0
    for i in range(1, N + 1):
        left: int = 0
        right: int = N + 1

        while right - left > 1:
            mid: int = (right + left) // 2

            if i * mid > K:
                right = mid
            else:
                left = mid

        answer += left

    print(answer)


if __name__ == "__main__":
    main()
