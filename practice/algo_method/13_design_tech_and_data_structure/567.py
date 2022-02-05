from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    L, R = map(int, input().split())

    answer: int = 0
    for i in range(L, R + 1):
        answer += (2 * i - 1) ** 2

    print(answer)


if __name__ == "__main__":
    main()
