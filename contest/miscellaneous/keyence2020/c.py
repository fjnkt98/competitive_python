from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K, S = map(int, input().split())
    if S < 1000000000:
        A: List[int] = [S] * K + [S + 1] * (N - K)
    else:
        A: List[int] = [S] * K + [1] * (N - K)

    print(*A)


if __name__ == "__main__":
    main()
