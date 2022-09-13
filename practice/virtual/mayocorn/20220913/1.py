from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    D: List[int] = list(map(int, input().split()))

    answer: int = 0
    for i, j in itertools.combinations(range(N), r=2):
        answer += D[i] * D[j]

    print(answer)


if __name__ == "__main__":
    main()
