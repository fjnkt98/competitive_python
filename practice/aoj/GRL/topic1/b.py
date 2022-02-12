from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M, r = map(int, input().split())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(M):
        s, t, d = map(int, input().split())
        graph[s].append((t, d))

    negative_cycle: bool = False
    distance: List[int] = [int(1e9) for i in range(N)]

    distance[r] = 0
    for i in range(N):
        update: bool = False
        for j in range(N):
            if distance[j] == int(1e9):
                continue

            for node, weight in graph[j]:
                if distance[node] > distance[j] + weight:
                    distance[node] = distance[j] + weight
                    update = True

        if not update:
            break

        if i == N - 1 and update:
            negative_cycle = True

    if negative_cycle:
        print("NEGATIVE CYCLE")
    else:
        for d in distance:
            if d == int(1e9):
                print("INF")
            else:
                print(d)


if __name__ == "__main__":
    main()
