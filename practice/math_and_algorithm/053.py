from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    answer: int = pow(4, N + 1, 1000000007) - 1
    answer = answer * pow(3, 1000000005, 1000000007)
    answer %= 1000000007

    print(answer)


if __name__ == "__main__":
    main()
