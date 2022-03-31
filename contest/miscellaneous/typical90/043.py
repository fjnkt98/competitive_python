from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    rs, cs = map(int, input().split())
    rs -= 1
    cs -= 1
    rt, ct = map(int, input().split())
    rt -= 1
    ct -= 1

    grid: List[str] = [input().rstrip() for i in range(H)]

    distance: List[List[int]] = [[1 << 60 for j in range(W)] for i in range(H)]

    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]

    candidate: Deque[Tuple[int, int, int, int]] = collections.deque()
    for i in range(4):
        distance[rs][cs] = 0
        candidate.append((rs, cs, i, 0))

    while candidate:
        r, c, dir, cost = candidate.popleft()

        if cost > distance[r][c]:
            continue

        for i in range(4):
            next_r: int = r + dr[i]
            next_c: int = c + dc[i]

            if 0 <= next_r < H and 0 <= next_c < W and grid[next_r][next_c] == ".":
                if dir != i:
                    if cost < distance[next_r][next_c]:
                        distance[next_r][next_c] = cost + 1
                        candidate.append((next_r, next_c, i, cost + 1))
                else:
                    if cost <= distance[next_r][next_c]:
                        distance[next_r][next_c] = cost
                        candidate.appendleft((next_r, next_c, i, cost))

    # for d in distance:
    #     print(*d)

    print(distance[rt][ct])


if __name__ == "__main__":
    main()
