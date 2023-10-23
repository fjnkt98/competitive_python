import sys
from dataclasses import dataclass

sys.setrecursionlimit(1000000)


@dataclass
class Edge:
    """
    Attributes
    - start: The index of the node at the start of this edge.
    - end: The index of the node at the end of this edge.
    - capacity: The capacity of this edge.
    - rev: The inverse edge of this is the `rev`-th one that the end node of this.
    """

    start: int
    end: int
    capacity: int
    rev: int


class FordFulkerson:
    """
    Ford-Fulkerson method implementation

    Attribute
    - n: The number of nodes in the graph.
    - m: The number of edges in the graph.
    - graph: Graph representation
    """

    def __init__(
        self,
        n: int,
        edges: list[tuple[int, int, int]],
    ) -> None:
        graph: list[list[Edge]] = [[] for _ in range(n)]
        for begin, end, capacity in edges:
            rev_from = len(graph[end])
            rev_to = len(graph[begin])
            graph[begin].append(Edge(begin, end, capacity, rev_from))
            graph[end].append(Edge(end, begin, 0, rev_to))

        self.n = n
        self.m = len(edges)
        self.graph = graph

    def dfs(
        self,
        explored: list[bool],
        current: int,
        goal: int,
        minimum_capacity: int,
    ) -> int:
        """
        Find s-t path on the current state of the graph returns the minimum capacity of the path.

        Update the edge and inverse edge corresponding it during explore.

        Args:
        - explored: The list of flags explored.
        - current: The index of the current node.
        - destination: The index of the goal node.
        - minimum_capacity: The minimum capacity exists on the path being explored.
        """
        if current == goal:
            return minimum_capacity

        explored[current] = True
        for e in self.graph[current]:
            if explored[e.end] or e.capacity == 0:
                continue

            flow = self.dfs(
                explored,
                e.end,
                goal,
                min(minimum_capacity, e.capacity),
            )
            if flow > 0:
                e.capacity -= flow
                self.graph[e.end][e.rev].capacity += flow
                return flow
        return 0

    def get_maximum_flow(self, start: int, goal: int) -> int:
        """
        Find maximum flow of the graph between start and goal.
        """
        maximum_flow = 0
        while True:
            explored = [False] * self.n

            flow = self.dfs(explored, start, goal, 1 << 60)
            if flow > 0:
                maximum_flow += flow
            else:
                break

        return maximum_flow


def main() -> None:
    N, M = map(int, input().split())
    edges: list[tuple[int, int, int]] = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a, b, c))

    ff = FordFulkerson(N, edges)
    print(ff.get_maximum_flow(0, N - 1))


if __name__ == "__main__":
    main()
