from typing import List, Tuple
import sys
import math
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X, Y = map(int, input().split())

    print(N // X + N // Y - N // (X * Y // math.gcd(X, Y)))


if __name__ == "__main__":
    main()
