from typing import List, Tuple
import sys
from array import array
import heapq


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def distance(s: str) -> int:
    return (ord("z") - ord(s) + 1) % 26


def advance(s: str, n: int) -> str:
    return chr(ord("a") + ((ord(s) - ord("a")) + n) % 26)


def main():
    S: str = input().rstrip()
    K: int = int(input())

    T: List[str] = list(S)
    for i, t in enumerate(T):
        d = distance(t)
        if d <= K:
            T[i] = advance(t, d)
            K -= d

    if K != 0:
        T[-1] = advance(T[-1], K)

    print("".join(T))


if __name__ == "__main__":
    main()
