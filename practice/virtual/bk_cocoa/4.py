from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math
import heapq


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


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
    N, M, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(M):
        a, b, t, k = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append((b, t, k))
        graph[b].append((a, t, k))

    distance: List[int] = [1 << 60 for i in range(N)]
    candidate: List[Tuple[int, int]] = [(0, X)]
    distance[X] = 0

    while candidate:
        d, node = heapq.heappop(candidate)

        if d > distance[node]:
            continue

        for next_node, weight, k in graph[node]:
            interval: int = k - (distance[node] % k) if (distance[node] % k) != 0 else 0
            if distance[next_node] > distance[node] + weight + interval:
                distance[next_node] = distance[node] + weight + interval
                heapq.heappush(candidate, (distance[next_node], next_node))

    print(distance[Y] if distance[Y] != 1 << 60 else -1)


if __name__ == "__main__":
    main()
