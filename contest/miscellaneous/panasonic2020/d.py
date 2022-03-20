from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(digit: int, N: int, S: str, answer: List[str]) -> None:
    if digit == N:
        answer.append(S)
        return

    biggest: int = ord("a")
    while chr(biggest) in S:
        biggest += 1
    biggest -= 1

    for code in range(ord("a"), biggest + 2):
        dfs(digit + 1, N, S + chr(code), answer)


def main():
    N: int = int(input())
    answer: List[str] = []

    dfs(0, N, "", answer)

    for a in sorted(answer):
        print(a)


if __name__ == "__main__":
    main()
