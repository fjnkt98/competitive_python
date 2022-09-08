from typing import *
import collections
import itertools
import bisect
import math
import numpy as np


def main():
    H, W = map(int, input().split())
    A: List[List[str]] = [
        list(map(lambda x: 0 if x == "." else 1, input())) for i in range(H)
    ]

    B: np.ndarary = np.array(A)
    cols: np.ndarray = np.sum(B, axis=0)
    rows: np.ndarray = np.sum(B, axis=1)
    for r in (B[rows > 0, :][:, cols > 0]).tolist():
        print("".join(map(lambda x: "#" if x == 1 else ".", r)))


if __name__ == "__main__":
    main()
