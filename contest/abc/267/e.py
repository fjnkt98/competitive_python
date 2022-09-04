from typing import *
import heapq


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    W: Dict[int, int] = {i: a for i, a in enumerate(A)}
    graph: List[Set[int]] = [set() for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].add(v)
        graph[v].add(u)

    cost: List[int] = [sum([W[node] for node in graph[i]]) for i in range(N)]
    eliminated: List[bool] = [False] * N

    candidate: List[Tuple[int, int]] = [(c, i) for i, c in enumerate(cost)]
    heapq.heapify(candidate)

    answer: int = 0
    while candidate:
        c, node = heapq.heappop(candidate)

        if eliminated[node]:
            continue

        for next_node in graph[node]:
            cost[next_node] -= A[node]
            heapq.heappush(candidate, (cost[next_node], next_node))

        answer = max(answer, c)
        eliminated[node] = True

    print(answer)


if __name__ == "__main__":
    main()
