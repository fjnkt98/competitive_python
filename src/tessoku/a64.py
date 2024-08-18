import heapq


class Dijkstra:
    """Dijkstra Method

    Dijkstra method implementation.

    Attributes:
        N (int): Number of the nodes in the graph.
        graph (list[list[tuple[int, int]]]): Adjacency-list representation of the graph.
        distance (list[int]): A list retains distance of the shortest path from start
                            to the node.
        previous (list[int]): A list retains previous node index of the node on the
                            shortest path.
    """

    def __init__(self, graph: list[list[tuple[int, int]]]) -> None:
        """Constructor

        Construct dijkstra object.

        Args:
            graph (list[list[tuple[int, int]]]): Adjacency-list representation of the
                                                graph.

        """

        # Copy the graph
        self.graph: list[list[tuple[int, int]]] = graph
        self.N: int = len(graph)

        # Initialize each list
        self.distance: list[int] = [1 << 60 for i in range(self.N)]
        self.previous: list[int] = [-1 for i in range(self.N)]

    def search(self, start_node: int) -> tuple[list[int], list[int]]:
        """Calculate distance of the shortest path from start_node to each nodes.

        Args:
            start_node (int): The index of the start node.

        Returns:
            list[int]: A list retains distance of the shortest path.
            list[int]: A list retains previous node of the node on the shortest path.

        """
        # Heap queue
        candidate: list[tuple[int, int]] = [(0, start_node)]
        # Set zero to the distance of the start node.
        self.distance[start_node] = 0

        # Start to search dijkstra
        while candidate:
            d, node = heapq.heappop(candidate)

            if d > self.distance[node]:
                continue

            for next_node, weight in self.graph[node]:
                if self.distance[next_node] > self.distance[node] + weight:
                    self.distance[next_node] = self.distance[node] + weight
                    self.previous[next_node] = node
                    heapq.heappush(
                        candidate, (self.distance[next_node], next_node)
                    )

        return (self.distance, self.previous)

    def restore_path(self, end_node: int) -> list[int]:
        """Get shortest path.

        Restore shortest path from start_node to end_node.

        Args:
            end_node (int): The index of the end node.

        Returns:
            list[int]: A list of the shortest path.

        """
        path: list[int] = []
        t: int = end_node
        while t != -1:
            path.append(t)
            t = self.previous[t]

        return list(reversed(path))


def main() -> None:
    N, M = map(int, input().split())
    graph: list[list[tuple[int, int]]] = [[] for i in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        graph[A].append((B, C))
        graph[B].append((A, C))

    dijkstra = Dijkstra(graph)
    distance, _ = dijkstra.search(0)
    for d in distance:
        if d == 1 << 60:
            print(-1)
        else:
            print(d)


if __name__ == "__main__":
    main()
