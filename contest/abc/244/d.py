from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S1, S2, S3 = input().split()
    T1, T2, T3 = input().split()

    S: str = S1 + S2 + S3
    T: str = T1 + T2 + T3

    if (
        (S1 == T1 and S2 == T2 and S3 == T3)
        or (S1 == T3 and S2 == T1 and S3 == T2)
        or (S1 == T2 and S2 == T3 and S3 == T1)
    ):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
