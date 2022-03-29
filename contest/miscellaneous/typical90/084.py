from typing import List, Tuple
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    S: str = input().rstrip()

    o: List[int] = [0] * N
    x: List[int] = [0] * N

    for i, s in enumerate(S):
        if s == "o":
            o[i] += 1
        else:
            x[i] += 1

    o = list(itertools.accumulate(o))
    x = list(itertools.accumulate(x))

    answer: int = 0
    for i, s in enumerate(S):
        if s == "o":
            answer += N - bisect.bisect_right(x, x[i])
        else:
            answer += N - bisect.bisect_right(o, o[i])

    print(answer)


if __name__ == "__main__":
    main()
