from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    M: str = bin(N)[2:]

    indices: List[int] = [i for i, m in enumerate(list(M)) if m == "1"]

    answer: List[int] = []
    for bits in itertools.product((0, 1), repeat=len(indices)):
        P: List[str] = ["0"] * len(M)
        for i, bit in enumerate(bits):
            if bit == 1:
                P[indices[i]] = "1"

        answer.append(int("".join(P), 2))

    for a in sorted(answer):
        print(a)


if __name__ == "__main__":
    main()
