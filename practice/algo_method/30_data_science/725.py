from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, A_bar, sigma_A, B_bar, sigma_B = map(int, input().split())
    print(sigma_B / sigma_A)


if __name__ == "__main__":
    main()
