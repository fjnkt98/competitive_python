from collections import deque


def main() -> None:
    N, M = map(int, input().split())
    graph: list[list[int]] = [[] for i in range(N)]
    for _ in range(M):
        A, B = map(lambda x: int(x) - 1, input().split())
        graph[A].append(B)
        graph[B].append(A)

    distance: list[int] = [-1] * N
    distance[0] = 0
    queue: deque[int] = deque()
    queue.append(0)

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                queue.append(next_node)

    for d in distance:
        print(d)


if __name__ == "__main__":
    main()
