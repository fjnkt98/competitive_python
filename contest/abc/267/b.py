from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()

    D: Dict[int, int] = {
        0: 3,
        1: 2,
        2: 4,
        3: 1,
        4: 3,
        5: 5,
        6: 0,
        7: 2,
        8: 4,
        9: 6,
    }

    C: List[int] = [0] * 7
    for i, s in enumerate(S):
        if s == "1":
            C[D[i]] += 1

    flag1: bool = True
    if S[0] == "1":
        flag1 = False

    for i, j in itertools.combinations(range(7), r=2):
        flag2: bool = False
        if C[i] >= 1 and C[j] >= 1:
            for k in range(i + 1, j):
                if C[k] == 0:
                    flag2 = True

        if flag1 and flag2:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
