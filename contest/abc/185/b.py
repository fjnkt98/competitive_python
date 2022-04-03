from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M, T = map(int, input().split())
    A: List[int] = [0] * M
    B: List[int] = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ok: bool = True
    battery: int = N
    last_time = 0
    for a, b in zip(A, B):
        battery -= a - last_time

        if battery <= 0:
            ok = False

        battery += b - a
        if battery >= N:
            battery = N

        last_time = b

    battery -= T - last_time
    if battery <= 0:
        ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
