from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    S: List[str] = [input() for i in range(2)]

    mod: int = 1000000007

    answer: int = 1
    x: int = 0
    previous_pattern: int = -1

    while x < N:
        if S[0][x] == S[1][x]:
            if previous_pattern == -1:
                answer *= 3
                answer %= mod
            elif previous_pattern == 0:
                answer *= 2
                answer %= mod
            previous_pattern = 0
            x += 1
        else:
            if previous_pattern == -1:
                answer *= 6
                answer %= mod
            elif previous_pattern == 0:
                answer *= 2
                answer %= mod
            else:
                answer *= 3
                answer %= mod
            previous_pattern = 1
            x += 2

    print(answer)


if __name__ == "__main__":
    main()
