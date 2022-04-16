from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S: str = input().rstrip()

    print("0" + S[0:3])


if __name__ == "__main__":
    main()
