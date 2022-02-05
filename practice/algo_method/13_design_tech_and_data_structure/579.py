from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N = int(input())
    A: List[int] = list(map(int, input().split()))

    answer: int = 1
    for a in A:
        answer *= a

    print(answer % 10)


if __name__ == "__main__":
    main()
