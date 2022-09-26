from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    left: int = 0
    right: int = K + 1
    while right - left > 1:
        mid: int = (right + left) >> 1

        M: int = 0
        for i, a in enumerate(A):
            if a >= mid:
                M += mid
            else:
                M += a
        if M <= K:
            left = mid
        else:
            right = mid

    for i in range(N):
        if A[i] >= left:
            K -= left
            A[i] -= left
        else:
            K -= A[i]
            A[i] = 0

    i: int = 0
    while K > 0:
        if A[i] > 0:
            K -= 1
            A[i] -= 1

        i += 1
        i %= N

    print(*A)


if __name__ == "__main__":
    main()
