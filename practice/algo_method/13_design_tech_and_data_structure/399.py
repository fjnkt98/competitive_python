from typing import List
import sys
from array import array
import bisect


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    W: array[int] = array("q", list(map(int, input().split())))

    V: array[int] = sorted(W)
    for w in W:
        print(bisect.bisect_left(V, w))


if __name__ == "__main__":
    main()
