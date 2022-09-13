from typing import *
import collections
import itertools
import bisect
import math


def main():
    A, B, K = map(int, input().split())

    if A >= K:
        print(A - K, B)
    else:
        K -= A
        A = 0

        if B <= K:
            print(0, 0)
        else:
            B -= K
            K = 0
            print(A, B)


if __name__ == "__main__":
    main()
