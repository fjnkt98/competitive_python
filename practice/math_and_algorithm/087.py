from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    answer: int = 1
    answer *= N * (N + 1) // 2
    answer %= 1000000007
    answer *= N * (N + 1) // 2
    answer %= 1000000007
    print(answer)


if __name__ == "__main__":
    main()
