from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    F: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    P: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    answer: int = int(-1e9)

    for bits in itertools.product((0, 1), repeat=10):
        if bits == tuple([0] * 10):
            continue

        profit: int = 0
        for f, p in zip(F, P):
            count: int = 0
            for i, bit in enumerate(bits):
                if bit == 1 and f[i] == 1:
                    count += 1
            profit += p[count]

        answer = max(answer, profit)

    print(answer)


if __name__ == "__main__":
    main()
