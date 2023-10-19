def main() -> None:
    N, M = map(int, input().split())
    graph: list[list[int]] = [[] for i in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A - 1].append(B - 1)
        graph[B - 1].append(A - 1)

    for i, nodes in enumerate(graph, start=1):
        print(f"{i}: {{{', '.join(map(lambda x: str(x + 1), sorted(nodes)))}}}")


if __name__ == "__main__":
    main()
