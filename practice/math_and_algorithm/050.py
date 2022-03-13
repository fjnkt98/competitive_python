from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    a, b = map(int, input().split())

    print(pow(a, b, 1000000007))


if __name__ == "__main__":
    main()
