from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    n, r = map(int, input().split())
    answer: int = 1
    for i in range(n, n - r, -1):
        answer *= i

    for i in range(1, r + 1):
        answer //= i

    print(answer)


if __name__ == "__main__":
    main()
