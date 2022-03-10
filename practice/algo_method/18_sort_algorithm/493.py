from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    L: List[Tuple[str, int, int, int]] = [() for i in range(N)]
    for i in range(N):
        S, A, B = input().split()
        L[i] = (S, int(A), int(B), -int(A) - int(B))

    L.sort(key=lambda x: (x[1], x[3]), reverse=True)

    for s, m, e, t in L:
        print(f"{s} {m} {e}")


if __name__ == "__main__":
    main()
