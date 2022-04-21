from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def encode(c: str) -> int:
    return ord(c) - ord("a")


def decode(x: int) -> str:
    return chr(x + ord("a"))


def main():
    S: str = input()
    T: str = input()

    F: List[List[int]] = [[-1] * 26 for i in range(26)]
    for s, t in zip(S, T):
        F[encode(s)][encode(t)] = 1

    ok: bool = True
    for i in range(26):
        count: int = 0
        for j in range(26):
            if F[i][j] == 1:
                count += 1

        if count >= 2:
            ok = False

    for j in range(26):
        count: int = 0
        for i in range(26):
            if F[i][j] == 1:
                count += 1

        if count >= 2:
            ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
