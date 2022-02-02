from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    answer: int = 0
    while N >= 5:
        N -= 5
        answer += 1

    while N >= 1:
        N -= 1
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
