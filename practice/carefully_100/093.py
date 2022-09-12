from typing import *
import collections
import itertools
import bisect
import math
import copy


def solve(K: int, G: List[List[int]], r: int, c: int) -> int:
    H: int = len(G)
    W: int = len(G[0])

    eliminated: List[List[bool]] = [[False for j in range(W)] for i in range(H)]
    eliminated[r][c] = True
    for j in range(W):
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

    score: int = 0
    step: int = 0
    while True:
        eliminated = [[False for j in range(W)] for i in range(H)]

        local_score: int = 0
        for i in range(H):
            index: int = 0
            for k, v in itertools.groupby(G[i]):
                L: List[int] = list(v)
                if k != -1 and len(L) >= K:
                    for l in range(index, index + len(L)):
                        eliminated[i][l] = True
                    local_score += k * len(L)
                index += len(L)

        if local_score == 0:
            break

        score += pow(2, step) * local_score

        for j in range(W):
            eliminate_count = 0
            col = []
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

        step += 1

    return score


def main():
    H, W, K = map(int, input().split())
    G: List[List[int]] = [list(map(int, input())) for i in range(H)]

    answer: int = 0
    for r, c in itertools.product(range(H), range(W)):
        answer = max(answer, solve(K, copy.deepcopy(G), r, c))

    print(answer)


if __name__ == "__main__":
    main()
