from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()
    T: str = input()

    print("Yes" if T.startswith(S) else "No")


if __name__ == "__main__":
    main()
