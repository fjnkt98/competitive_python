from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A: List[int] = list(map(int, input().split()))

    print(sum(A) % 100)


if __name__ == "__main__":
    main()
