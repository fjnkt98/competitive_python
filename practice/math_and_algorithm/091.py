from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X = map(int, input().split())

    answer: int = 0
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            c: int = X - a - b
            if b < c <= N:
                answer += 1

    print(answer)


if __name__ == "__main__":
    main()
