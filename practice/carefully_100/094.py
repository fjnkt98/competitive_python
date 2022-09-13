from typing import *
import collections
import itertools
import bisect
import math


class Node:
    def __init__(self, w: int, d: int):
        self.w: int = w
        self.d: int = d
        self.left_child: Union[Node, None] = None
        self.right_child: Optional[Node] = None

    @property
    def area(self) -> int:
        return self.w * self.d


def solve(N: int, W: int, D: int, P: List[int], S: List[int]) -> List[int]:
    root = Node(W, D)
    pieces: List[Node] = [root]

    for p, s in zip(P, S):
        node: Node = pieces.pop(p - 1)

        E: List[int] = [0] + list(itertools.accumulate([node.w, node.d] * 2))
        s %= 2 * node.w + 2 * node.d

        if E[0] < s < E[1]:
            # 縦切り
            left = Node(s, node.d)
            right = Node(node.w - s, node.d)

            if left.area > right.area:
                left, right = right, left

            pieces.append(left)
            pieces.append(right)
            node.left_child = left
            node.right_child = right

        elif E[1] < s < E[2]:
            # 横切り
            left = Node(node.w, s - E[1])
            right = Node(node.w, E[2] - s)

            if left.area > right.area:
                left, right = right, left

            pieces.append(left)
            pieces.append(right)
            node.left_child = left
            node.right_child = right

        elif E[2] < s < E[3]:
            # 縦切り
            left = Node(s - E[2], node.d)
            right = Node(E[3] - s, node.d)

            if left.area > right.area:
                left, right = right, left

            pieces.append(left)
            pieces.append(right)
            node.left_child = left
            node.right_child = right

        elif E[2] < s < E[4]:
            # 横切り
            left = Node(node.w, s - E[3])
            right = Node(node.w, E[4] - s)

            if left.area > right.area:
                left, right = right, left

            pieces.append(left)
            pieces.append(right)
            node.left_child = left
            node.right_child = right

    return sorted([p.area for p in pieces])


def main():
    answers: List[List[int]] = []
    while True:
        N, W, D = map(int, input().split())
        if (N, W, D) == (0, 0, 0):
            break
        if N == 0:
            P = []
            S = []
        else:
            P, S = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

        answers.append(solve(N, W, D, P, S))

    for answer in answers:
        print(*answer)


if __name__ == "__main__":
    main()
