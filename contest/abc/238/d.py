from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    T: int = int(input())

    for i in range(T):
        a, s = map(int, input().split())
        if s - 2 * a >= 0 and (s - 2 * a) & a == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
