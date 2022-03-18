from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    if c - a - b < 0:
        print("No")
    else:
        if 4 * a * b < (c - a - b) ** 2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
