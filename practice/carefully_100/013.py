from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    answer: int = 0
    for bits in itertools.product((0, 1), repeat=H):
        B: np.ndarray = np.array(A)
        for i, bit in enumerate(bits):
            if bit == 1:
                B[i] = 1 - B[i]

        C: np.ndarray = np.count_nonzero(B, axis=0)
        D: np.ndarray = H - C
        answer = max(answer, H * W - np.sum(np.min(np.stack([C, D]), axis=0)))

    print(answer)


if __name__ == "__main__":
    main()
