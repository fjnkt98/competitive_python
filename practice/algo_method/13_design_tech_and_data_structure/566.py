from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    answer: int = 0
    for i in range(1, N + 1):
        answer += i

    print(answer)


if __name__ == "__main__":
    main()
