import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main() -> None:
    N, M = map(int, input().split())
    graph: list[list[int]] = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    for i in range(N):
        graph[i].sort()

    for i, l in enumerate(graph):
        cities = [j + 1 for j in l]
        print(len(cities), *cities)


if __name__ == "__main__":
    main()
