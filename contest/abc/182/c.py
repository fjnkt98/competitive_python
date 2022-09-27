from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: str = input()

    answer: int = 1 << 60
    for bits in itertools.product((0, 1), repeat=len(N)):
        if bits == tuple([0] * len(N)):
            continue

        M: List[str] = []
        for i, bit in enumerate(bits):
            if bit == 1:
                M.append(N[i])

        if int("".join(M)) % 3 == 0:
            answer = min(answer, bits.count(0))

    print(answer if answer != 1 << 60 else -1)


if __name__ == "__main__":
    main()
