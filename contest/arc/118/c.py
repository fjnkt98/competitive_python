from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    S: List[int] = [6, 10, 15]
    if N == 3:
        print(*S)
        return
    A: List[int] = set(S)
    for s in S:
        k: int = 2 * s
        while k <= 10000:
            A.add(k)
            if len(A) == N:
                break
            k += s
        if len(A) == N:
            break

    print(*A)


if __name__ == "__main__":
    main()
