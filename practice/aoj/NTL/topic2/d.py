from typing import List
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    if A == 0:
        print(0)
        return

    a_sign: int = 1 if A > 0 else -1
    b_sign: int = 1 if B > 0 else -1

    print(a_sign * b_sign * (abs(A) // abs(B)))


if __name__ == "__main__":
    main()
