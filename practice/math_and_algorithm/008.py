from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, S = map(int, input().split())

    answer: int = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i + j <= S:
                answer += 1

    print(answer)


if __name__ == "__main__":
    main()
