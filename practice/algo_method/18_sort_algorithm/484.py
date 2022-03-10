from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    A.sort(reverse=True)
    print(sum(A[:K]))


if __name__ == "__main__":
    main()
