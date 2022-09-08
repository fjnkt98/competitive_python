from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: str = input()

    answer: int = 0
    for bits in itertools.product((0, 1), repeat=len(N)):
        M: List[str] = []

        for i, bit in enumerate(bits):
            if bit == 1:
                M.append(N[i])

        if M and int("".join(M)) % 3 == 0:
            answer = max(answer, len(M))

    if answer == 0:
        print(-1)
    else:
        print(len(N) - answer)


if __name__ == "__main__":
    main()
