from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()
    C = collections.Counter()
    for i in range(len(S) - 1):
        C[S[i] + S[i + 1]] += 1

    D = C.most_common()
    M: int = D[0][1]
    E: List[str] = sorted([k for k, v in C.items() if v == M])
    print(E[0])


if __name__ == "__main__":
    main()
