from typing import *
import collections
import itertools
import bisect
import math


def solve(H: int, G: List[List[int]]) -> int:
    score: int = 0
    while True:
        local_score: int = 0
        eliminated: List[List[bool]] = [[False for j in range(5)] for i in range(H)]
        for i, row in enumerate(G):
            index: int = 0
            for k, v in itertools.groupby(row):
                L: List[int] = list(v)
                if (k != -1) and (len(L) >= 3):
                    for l in range(index, index + len(L)):
                        eliminated[i][l] = True
                    local_score += k * len(L)
                index += len(L)

        if local_score == 0:
            break

        score += local_score

        for j in range(5):
            eliminate_count: int = 0
            col: List[int] = []
            for i in range(H):
                if eliminated[i][j]:
                    eliminate_count += 1
                else:
                    col.append(G[i][j])

            if eliminate_count == 0:
                continue
            for i in range(H):
                if i < eliminate_count:
                    G[i][j] = -1
                else:
                    G[i][j] = col[i - eliminate_count]

    return score


def main():
    answer: List[int] = []
    while True:
        H: int = int(input())
        if H == 0:
            break
        G: List[List[int]] = [list(map(int, input().split())) for i in range(H)]
        answer.append(solve(H, G))

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
