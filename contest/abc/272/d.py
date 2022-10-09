from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())

    nexts: List[Tuple[int, int]] = []
    m: int = math.ceil(math.sqrt(M))
    for i, j in itertools.product(range(-m, m + 1), repeat=2):
        if i ** 2 + j ** 2 == M:
            nexts.append((i, j))

    G: List[List[int]] = [[-1] * N for i in range(N)]
    G[0][0] = 0
    candidate = collections.deque([(0, 0)])
    while candidate:
        r, c = candidate.popleft()

        for ni, nj in nexts:
            nr: int = r + ni
            nc: int = c + nj

            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == -1:
                G[nr][nc] = G[r][c] + 1
                candidate.append((nr, nc))

    for r in G:
        print(*r)


if __name__ == "__main__":
    main()
