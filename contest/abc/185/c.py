from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(n: int, r: int) -> int:
    R: List[int] = list(reversed(range(2, r + 1)))

    result: int = 1
    for i in range(n, n - r, -1):
        result *= i

        if R and result % R[-1] == 0:
            result //= R.pop()

    return result


def main():
    L: int = int(input())

    print(f(L - 1, 11))


if __name__ == "__main__":
    main()
