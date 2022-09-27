from typing import *
import collections
import itertools
import bisect
import math


def main():
    X, Y, A, B = map(int, input().split())

    experience: int = 0
    strength: int = X
    while A * strength < Y and A * strength <= strength + B:
        strength *= A
        experience += 1

    C: int = (Y - strength - 1) // B
    experience += C
    strength += B * C

    print(experience)


if __name__ == "__main__":
    main()
