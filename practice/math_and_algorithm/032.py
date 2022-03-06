from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    print("Yes" if X in A else "No")


if __name__ == "__main__":
    main()
