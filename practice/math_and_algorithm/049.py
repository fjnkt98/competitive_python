from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    mod: int = 1000000007
    N: int = int(input())

    fibonacci: List[int] = [1 for i in range(N)]
    for i in range(2, N):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci[i] %= mod

    print(fibonacci[N - 1])


if __name__ == "__main__":
    main()
