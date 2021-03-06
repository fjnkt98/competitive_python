from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X, Y = map(int, input().split())

    if abs(X) + abs(Y) <= N:
        if (X + Y) % 2 == N % 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == "__main__":
    main()
