from typing import List, Deque, Tuple
from sys import setrecursionlimit
import collections


setrecursionlimit(10000)


def main():
    H, W = map(int, input().split())
    X0, Y0, X1, Y1 = map(int, input().split())
    G: List[str] = [input() for i in range(H)]

    distance: List[List[int]] = [[-1 for j in range(W)] for i in range(H)]

    distance[X0][Y0] = 0

    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]

    candidate: Deque[Tuple[int, int]] = collections.deque()
    candidate.append((X0, Y0))
    while candidate:
        node: Tuple[int, int] = candidate.popleft()
        r: int = node[0]
        c: int = node[1]

        for i in range(4):
            next_r: int = r + dr[i]
            next_c: int = c + dc[i]

            if 0 <= next_r < H and 0 <= next_c < W and G[next_r][next_c] == "W":
                if distance[next_r][next_c] != -1:
                    continue
                distance[next_r][next_c] = distance[r][c] + 1
                candidate.append((next_r, next_c))

    print(distance[X1][Y1])


if __name__ == "__main__":
    main()
