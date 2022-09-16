from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    for i in range(N, 1000):
        if len(set(str(i))) == 1:
            print(i)
            break


if __name__ == "__main__":
    main()
