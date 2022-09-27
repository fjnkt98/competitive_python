from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    H: List[int] = sorted(list(map(int, input().split())))
    W: List[int] = list(map(int, input().split()))

    Al: List[int] = [0] * (N + 1)
    for i in range(1, N, 2):
        Al[i] = H[i] - H[i - 1]
    Cl = list(itertools.accumulate(Al))

    Ar: List[int] = [0] * (N + 1)
    for i in range(N - 2, 0, -2):
        Ar[i] = H[i + 1] - H[i]
    Cr = list(reversed(list(itertools.accumulate(reversed(Ar)))))

    answer: int = 1 << 60
    for w in W:
        index: int = bisect.bisect_left(H, w)
        result: int = 0
        if index % 2 == 0:
            result = Cl[index] + Cr[index + 1] + abs(H[index] - w)
        else:
            result = Cl[index - 1] + Cr[index] + abs(w - H[index - 1])

        answer = min(answer, result)

    print(answer)


if __name__ == "__main__":
    main()
