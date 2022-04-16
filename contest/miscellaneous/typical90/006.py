from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N, K = map(int, input().split())
    S: str = input()

    c: List[List[int]] = [[0] * 26 for i in range(N + 1)]
    c[len(S)] = [len(S)] * 26

    for i in range(N - 1, -1, -1):
        for j in range(26):
            if (ord(S[i]) - ord("a")) == j:
                c[i][j] = i
            else:
                c[i][j] = c[i + 1][j]

    answer: List[str] = []
    current_position: int = 0
    for i in range(1, K + 1):
        for j in range(26):
            next_position: int = c[current_position][j]
            max_possible_length: int = len(S) - next_position - 1 + i
            if max_possible_length >= K:
                answer.append(chr(ord("a") + j))
                current_position = next_position + 1
                break

    print("".join(answer))


if __name__ == "__main__":
    main()
