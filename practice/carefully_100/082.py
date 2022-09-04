from typing import *
import collections
import itertools
import bisect
import math


def main():
    answers: List[int] = []
    while True:
        N: int = int(input())
        if N == 0:
            break

        def parse(S: str) -> int:
            T: List[int] = list(map(int, S.split(":")))
            return T[0] * 3600 + T[1] * 60 + T[2]

        T = [tuple(map(parse, input().split())) for i in range(N)]

        C: List[int] = [0 for i in range(86402)]
        for s, t in T:
            C[s] += 1
            C[t] -= 1
        C = list(itertools.accumulate(C))
        answers.append(max(C))

    for a in answers:
        print(a)


if __name__ == "__main__":
    main()
