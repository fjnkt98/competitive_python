from typing import *
import collections
import itertools
import bisect
import math


def sign(x: int) -> int:
    return x // abs(x)


def main():
    X, Y, Z = map(int, input().split())

    if sign(X) == sign(Y):
        if abs(X) < abs(Y):
            print(abs(X))
            return

        if abs(Y) < abs(Z):
            print(-1)
            return
        else:
            if sign(Y) == sign(Z):
                print(abs(X))
                return
            else:
                print(2 * abs(Z) + abs(X))
    else:
        print(abs(X))
        return


if __name__ == "__main__":
    main()
