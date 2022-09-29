from typing import *
import collections
import itertools
import bisect
import math


def main():
    X, A, B, C = map(int, input().split())

    rabbit = (X + A * C) / A
    turtle = X / B

    if abs(rabbit - turtle) < 1e-8:
        print("Tie")
    elif rabbit < turtle:
        print("Hare")
    else:
        print("Tortoise")


if __name__ == "__main__":
    main()
