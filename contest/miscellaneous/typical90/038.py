from typing import List, Tuple
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    gcd: int = math.gcd(A, B)

    lcm: int = A * (B // gcd)

    if lcm > 1000000000000000000:
        print("Large")
    else:
        print(lcm)


if __name__ == "__main__":
    main()
