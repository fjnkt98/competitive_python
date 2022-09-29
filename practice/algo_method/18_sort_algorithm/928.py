from typing import *
import collections
import itertools
import bisect
import math
import operator


def main():
    N: int = int(input())
    I: List[Tuple[int, int]] = sorted(
        [tuple(map(int, input().split())) for i in range(N)], key=operator.itemgetter(1)
    )

    last: int = 0
    count: int = 0
    for i, (l, r) in enumerate(I):
        if last <= l:
            count += 1
            last = r

    print("Yes" if count == N else "No")


if __name__ == "__main__":
    main()
