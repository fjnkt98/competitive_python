from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, C = map(int, input().split())
    T, A = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    answer: List[int] = [0] * N
    for k in range(30):
        f: Tuple[int, int] = (0, 1)

        bit: int = (C >> k) & 1
        for i, (t, a) in enumerate(zip(T, A)):
            x: int = (a >> k) & 1
            if t == 1:
                g = (x & 0, x & 1)
            elif t == 2:
                g = (x | 0, x | 1)
            else:
                g = (x ^ 0, x ^ 1)

            f = (g[f[0]], g[f[1]])
            bit = f[bit]
            answer[i] |= bit << k

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
