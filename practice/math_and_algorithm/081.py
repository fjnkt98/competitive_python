from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    answer: int = 0

    for i in [10000, 5000, 1000]:
        while N >= i:
            N -= i
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
