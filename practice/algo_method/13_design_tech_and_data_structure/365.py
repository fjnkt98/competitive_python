from typing import List, Set
import sys
import math


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N = int(input())
    P: List[List[int, int]] = [list(map(int, input().split())) for i in range(N)]

    answer: float = 0.0

    visited: Set[int] = set([0])

    previous_node: int = 0

    def get_distance(i: int, j: int) -> float:
        return math.sqrt(pow(P[i][0] - P[j][0], 2) + pow(P[i][1] - P[j][1], 2))

    for i in range(N - 1):
        minimum_distance, next_node = min(
            [(get_distance(previous_node, j), j) for j in range(N) if j not in visited]
        )

        visited.add(next_node)
        answer += minimum_distance

        previous_node = next_node

    answer += get_distance(previous_node, 0)

    print(answer)


if __name__ == "__main__":
    main()
