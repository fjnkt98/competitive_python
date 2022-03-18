from typing import List, Tuple
import sys
from array import array
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    A //= math.gcd(A, B)

    if A > 1000000000000000000 // B:
        print("Large")
    else:
        print(A * B)


if __name__ == "__main__":
    main()
