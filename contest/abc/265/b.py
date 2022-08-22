from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M, T = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    if M != 0:
        X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(M)]))

    bonus: Dict[int, int] = {x - 1: y for x, y in zip(X, Y)} if M != 0 else {}

    ok: bool = True
    position: int = 0
    while position < N - 1:
        T -= A[position]
        if T <= 0:
            ok = False
            break

        position += 1

        if position in bonus:
            T += bonus[position]

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
