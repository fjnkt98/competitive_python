from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    answer: float = 0.0
    for i in range(N):
        answer += N / (N - i)

    print(answer)


if __name__ == "__main__":
    main()
