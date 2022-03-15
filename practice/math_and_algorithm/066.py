from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    C: int = 0
    for a in range(1, N + 1):
        for b in range(max(1, a - (K - 1)), min(N, a + (K - 1)) + 1):
            for c in range(max(1, a - (K - 1)), min(N, a + (K - 1)) + 1):
                if abs(b - c) < K:
                    C += 1

    print(N ** 3 - C)


if __name__ == "__main__":
    main()
