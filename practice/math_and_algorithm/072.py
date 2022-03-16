from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    answer: int = 0
    for i in range(1, B + 1):
        if (B // i) - ((A + i - 1) // i) >= 1:
            answer = i

    print(answer)


if __name__ == "__main__":
    main()
