from typing import List, Tuple
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    gcd: int = math.gcd(A, math.gcd(B, C))

    answer: int = 0
    answer += A // gcd - 1
    answer += B // gcd - 1
    answer += C // gcd - 1

    print(answer)


if __name__ == "__main__":
    main()
