from typing import List, Tuple
import sys
from array import array
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    answer = A[0]
    for a in A:
        answer = math.gcd(answer, a)

    print(answer)


if __name__ == "__main__":
    main()
