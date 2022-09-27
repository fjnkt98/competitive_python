from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    X: List[int] = list(map(int, input().split()))

    manhattan: int = sum([abs(x) for x in X])
    euclid: float = math.sqrt(sum([x ** 2 for x in X]))
    tchebichef: int = max([abs(x) for x in X])

    print(manhattan)
    print(euclid)
    print(tchebichef)


if __name__ == "__main__":
    main()
