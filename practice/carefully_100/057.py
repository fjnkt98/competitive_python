from typing import *
import collections
import itertools
import bisect
import math
import heapq


class Dijkstra:
    """Dijkstra Method

    Dijkstra method implementation.

    Attributes:
        N (int): Number of the nodes in the graph.
        graph (List[List[Tuple[int, int]]]): Adjacency-list representation of the graph.
        distance (List[int]): A list retains distance of the shortest path from start
                            to the node.
        previous (List[int]): A list retains previous node index of the node on the
                            shortest path.
    """

    def __init__(self, graph: List[List[Tuple[int, int]]]):
        """Constructor

        Construct dijkstra object.

        Args:
            graph (List[List[Tuple[int, int]]]): Adjacency-list representation of the
                                                graph.

        """

        # Copy the graph
        self.graph: List[List[Tuple[int, int]]] = graph
        self.N: int = len(graph)

        # Initialize each list
        self.distance: List[int] = [1 << 60 for i in range(self.N)]
        self.previous: List[int] = [-1 for i in range(self.N)]

    def search(self, start_node: int) -> Tuple[List[int], List[int]]:
        """Calculate distance of the shortest path from start_node to each nodes.

        Args:
            start_node (int): The index of the start node.

        Returns:
            List[int]: A list retains distance of the shortest path.
            List[int]: A list retains previous node of the node on the shortest path.

        """
        # Heap queue
        candidate: List[Tuple[int, int]] = [(0, start_node)]
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
                    heapq.heappush(candidate, (self.distance[next_node], next_node))

        return (self.distance, self.previous)

    def restore_path(self, end_node: int) -> List[int]:
        """Get shortest path.

        Restore shortest path from start_node to end_node.

        Args:
            end_node (int): The index of the end node.

        Returns:
            List[int]: A list of the shortest path.

        """
        path: List[int] = []
        t: int = end_node
        while t != -1:
            path.append(t)
            t = self.previous[t]

        return list(reversed(path))


def main():
    N, K = map(int, input().split())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for _ in range(K):
        k = list(map(int, input().split()))
        if k[0] == 0:
            a, b = k[1:]
            a -= 1
            b -= 1

            dijkstra = Dijkstra(graph)
            distance, _ = dijkstra.search(a)

            print(distance[b] if distance[b] != 1 << 60 else -1)
        else:
            c, d, e = k[1:]
            c -= 1
            d -= 1
            graph[c].append((d, e))
            graph[d].append((c, e))


if __name__ == "__main__":
    main()
