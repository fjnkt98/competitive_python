from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import copy


sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N: int = 8


def dfs(
    r: int,
    board: List[List[bool]],
    row: List[int],
    col: List[bool],
    left: List[bool],
    right: List[bool],
) -> None:
    if r == N:
        for i, j in itertools.product(range(N), repeat=2):
            if board[i][j] and row[i] != j:
                return

        for i, j in enumerate(row):
            board[i][j] = True

        for b in board:
            print(*list(map(lambda x: "Q" if x else ".", b)), sep="")

        return

    for c in range(N):
        if col[c] or left[r + c] or right[r - c + N - 1]:
            continue
        row[r] = c
        col[c] = True
        left[r + c] = True
        right[r - c + N - 1] = True

        dfs(r + 1, board, row, col, left, right)

        row[r] = -1
        col[c] = False
        left[r + c] = False
        right[r - c + N - 1] = False


def main():
    K: int = int(input())
    A: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(K)]

    row: List[int] = [-1] * N
    col: List[bool] = [False] * N
    left: List[bool] = [False] * (2 * N - 1)
    right: List[bool] = [False] * (2 * N - 1)

    X: List[List[bool]] = [[False] * N for i in range(N)]
    for (r, c) in A:
        X[r][c] = True

    dfs(0, X, row, col, left, right)


if __name__ == "__main__":
    main()
