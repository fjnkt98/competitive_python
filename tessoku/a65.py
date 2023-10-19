import sys

sys.setrecursionlimit(1000000)


def search(
    graph: list[list[int]],
    count: list[int],
    current: int,
    previous: int,
) -> int:
    c = 0

    for next_node in graph[current]:
        if next_node == previous:
            continue
        c += search(graph, count, next_node, current) + 1

    count[current] = c
    return c


def main() -> None:
    N: int = int(input())
    A: list[int] = [int(v.strip()) - 1 for v in input().split()]

    graph: list[list[int]] = [[] for i in range(N)]
    for i, a in enumerate(A, start=1):
        graph[i].append(a)
        graph[a].append(i)

    answer = [0] * N
    search(graph, answer, 0, -1)
    print(*answer)


if __name__ == "__main__":
    main()
