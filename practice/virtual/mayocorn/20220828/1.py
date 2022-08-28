from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    S: str = input()

    T: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(S)]
    print(len(T))


if __name__ == "__main__":
    main()
