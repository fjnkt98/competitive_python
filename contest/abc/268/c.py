from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    P: List[int] = list(map(int, input().split()))

    C: List[int] = [0] * N
    for i in range(N):
        C[(P[i] - i + 1) % N] += 1
        C[(P[i] - i) % N] += 1
        C[(P[i] - i - 1) % N] += 1

    print(max(C))


if __name__ == "__main__":
    main()
