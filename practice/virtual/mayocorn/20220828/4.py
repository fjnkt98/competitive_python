from typing import *
import collections
import itertools
import bisect
import math
import numpy as np


def encode(c: str) -> int:
    return ord(c) - ord("a")


def decode(x: int) -> str:
    return chr(x + ord("a"))


def main():
    S: str = input()
    T: str = input()

    F: List[List[int]] = [[0] * 26 for i in range(26)]
    for s, t in zip(S, T):
        F[encode(s)][encode(t)] = 1

    G: np.ndarray = np.array(F, dtype=np.int64)

    ok: bool = True
    for i in range(26):
        if np.sum(G[i, :]) >= 2:
            ok = False

    for j in range(26):
        if np.sum(G[:, j]) >= 2:
            ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
