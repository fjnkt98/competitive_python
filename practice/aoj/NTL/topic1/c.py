from typing import List
import sys
from array import array
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A: List[int] = list(map(int, input().split()))

    gcd: int = A[0]
    lcm: int = A[0]
    for a in A:
        gcd = math.gcd(lcm, a)
        lcm = lcm * a // gcd

    print(lcm)


if __name__ == "__main__":
    main()
