from typing import *
import collections
import itertools
import bisect
import math
import numpy as np


def main():
    H1, W1 = map(int, input().split())
    A: np.ndarray = np.array(
        [list(map(int, input().split())) for i in range(H1)], dtype=np.int64
    )
    H2, W2 = map(int, input().split())
    B: np.ndarray = np.array(
        [list(map(int, input().split())) for i in range(H2)], dtype=np.int64
    )

    for rows in itertools.combinations(range(H1), r=H2):
        for cols in itertools.combinations(range(W1), r=W2):
            if np.array_equal(A[rows, :][:, cols], B):
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
