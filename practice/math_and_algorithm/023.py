from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    B: List[int] = list(map(int, input().split()))
    R: List[int] = list(map(int, input().split()))

    answer: float = sum(B) / N + sum(R) / N
    print(answer)


if __name__ == "__main__":
    main()
