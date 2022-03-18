from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X, Y = map(int, input().split())

    for a in range(1, N + 1):
        for b in range(a, N + 1):
            for c in range(b, N + 1):
                d: int = X - a - b - c
                if d < 0 or d > N:
                    continue
                if a * b * c * d == Y:
                    print("Yes")
                    return

    print("No")
    return


if __name__ == "__main__":
    main()
