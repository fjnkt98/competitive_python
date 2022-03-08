from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    answer: int = 0
    for i in range(1, N + 1):
        k = N // i
        answer += k * (k + 1) * i // 2

    print(answer)


if __name__ == "__main__":
    main()
