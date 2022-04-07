from typing import List, Tuple
import sys
import collections
import itertools
import operator


sys.setrecursionlimit(1000000)
# input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    P: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    P.sort(key=operator.itemgetter(0))

    answer: int = 0
    for a, b in P:
        if M > b:
            answer += a * b
            M -= b
        else:
            answer += a * M
            M = 0
            break

    print(answer)


if __name__ == "__main__":
    main()
