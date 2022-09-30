from typing import *
import collections
import itertools
import bisect
import math


def main():
    O: str = input()
    E: str = input()

    N: int = len(O) + len(E)
    S: List[str] = [""] * N
    for i in range(N):
        if i % 2 == 0:
            S.append(O[i // 2])
        else:
            S.append(E[i // 2])

    print("".join(S))


if __name__ == "__main__":
    main()
