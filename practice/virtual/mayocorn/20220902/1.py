from typing import *
import collections
import itertools
import bisect
import math


def main():
    X: str = input()

    if "." in X:
        print(X[: X.find(".")])
    else:
        print(X)


if __name__ == "__main__":
    main()
