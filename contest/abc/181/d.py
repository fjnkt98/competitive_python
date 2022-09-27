from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()

    C = collections.Counter(S)
    A: List[int] = []
    for k, v in C.items():
        if v >= 3:
            A.extend([str(k)] * 3)
        else:
            A.extend([str(k)] * v)

    if len(A) < 3:
        for a in itertools.permutations(A):
            if int("".join(a)) % 8 == 0:
                print("Yes")
                return
        print("No")
        return

    for i, j, k in itertools.product(range(len(A)), repeat=3):
        if i == j or j == k or k == i:
            continue
        if int("".join([A[i], A[j], A[k]])) % 8 == 0:
            print("Yes")
            return

    print("No")
    return


if __name__ == "__main__":
    main()
