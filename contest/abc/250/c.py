from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    X: List[int] = [int(input()) - 1 for i in range(Q)]

    position: List[int] = list(range(N))
    label: List[int] = list(range(N))

    for x in X:
        if position[x] != N - 1:
            left_position: int = position[x]
            right_position: int = position[x] + 1

            left_label: int = x
            right_label: int = label[right_position]

            label[left_position] = right_label
            label[right_position] = left_label

            position[left_label] = right_position
            position[right_label] = left_position

        else:
            right_position: int = position[x]
            left_position: int = position[x] - 1

            right_label: int = x
            left_label: int = label[left_position]

            label[left_position] = right_label
            label[right_position] = left_label

            position[left_label] = right_position
            position[right_label] = left_position

    print(*list(map(lambda x: x + 1, label)))


if __name__ == "__main__":
    main()
