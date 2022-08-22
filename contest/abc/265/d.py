from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, P, Q, R = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    C: List[int] = [0] + list(itertools.accumulate(A))

    candidates: List[Tuple[int, int]] = []
    for l in range(1, N):
        r: int = bisect.bisect_left(C, P + Q + R + C[l - 1])

        if r > N or C[r] - C[l - 1] != P + Q + R:
            continue

        candidates.append((l, r + 1))

    for x, w in candidates:
        y: int = bisect.bisect_right(C, P + C[x - 1])
        if not (x < y < w) or not (C[y - 1] - C[x - 1] == P):
            continue

        z: int = bisect.bisect_right(C, Q + C[y - 1])
        if not (y < z < w) or not (C[z - 1] - C[y - 1] == Q):
            continue

        if (
            C[y - 1] - C[x - 1] == P
            and C[z - 1] - C[y - 1] == Q
            and C[w - 1] - C[z - 1] == R
        ):
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
