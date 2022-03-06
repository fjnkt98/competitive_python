from typing import List, Tuple
import sys
from array import array
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    answer: int = A[0]
    gcd: int = A[0]
    lcm: int = A[0]

    for a in A[1:]:
        lcm = lcm * a // math.gcd(lcm, a)

    print(lcm)


if __name__ == "__main__":
    main()
