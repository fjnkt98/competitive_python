def main() -> None:
    N, M = map(int, input().split())
    graph: list[list[int]] = [[] for i in range(N)]
    for _ in range(M):
        A, B = map(lambda x: int(x) - 1, input().split())
        graph[A].append(B)
        graph[B].append(A)

    explored: list[bool] = [False] * N
    explored[0] = True
    stack: list[int] = [0]
    while stack:
        node = stack.pop()
        explored[node] = True
        for next_node in graph[node]:
            if not explored[next_node]:
                stack.append(next_node)

    if all(explored):
        print("The graph is connected.")
    else:
        print("The graph is not connected.")


if __name__ == "__main__":
    main()
