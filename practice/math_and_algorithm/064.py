from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    total_diff: int = sum(A)
    if total_diff <= K and (K - total_diff) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
