from typing import List
import sys
from array import array


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    A: array[int] = array("q", list(map(int, input().split())))

    print(A)

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
