from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    mod: int = 1000000007

    answer: int = 0
    for i, a in enumerate(A):
        answer += a * pow(2, i, mod)
        answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
