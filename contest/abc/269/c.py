from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    X: str = bin(N)[2:]
    C: int = X.count("1")
    D: List[int] = [i for i, b in enumerate(X) if b == "1"]

    answers: List[int] = []
    for bits in itertools.product((0, 1), repeat=C):
        S: List[str] = ["0"] * len(X)
        for i, bit in enumerate(bits):
            if bit == 1:
                S[D[i]] = "1"
        answers.append(int("".join(S), 2))

    answers.sort()
    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
