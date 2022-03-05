from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline().rstrip


def main():
    N: int = int(input())

    coins: List[int] = [25, 10, 5, 1]
    answer: int = 0
    for c in coins:
        answer += N // c
        N %= c

    print(answer)


if __name__ == "__main__":
    main()
