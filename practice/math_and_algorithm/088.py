from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    answer: int = 1
    answer *= A * (A + 1) // 2
    answer %= 998244353
    answer *= B * (B + 1) // 2
    answer %= 998244353
    answer *= C * (C + 1) // 2
    answer %= 998244353

    print(answer)


if __name__ == "__main__":
    main()
