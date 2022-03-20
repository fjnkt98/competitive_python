from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def run_length(S: str) -> List[Tuple[str, int]]:
    grouped = itertools.groupby(S)
    result: List[Tuple[str, int]] = []

    for key, value in grouped:
        result.append((key, len(list(value))))

    return result


def main():
    S: str = input().rstrip()
    K: int = int(input())

    answer: int = 0
    T = run_length(S)

    if len(T) == 1:
        answer = K * T[0][1] // 2
    else:
        for key, value in T:
            answer += value // 2
        answer *= K

        if S[0] == S[-1]:
            a: int = T[0][1]
            b: int = T[-1][1]
            sub: int = a // 2 + b // 2 - (a + b) // 2

            answer -= sub * (K - 1)

    print(answer)


if __name__ == "__main__":
    main()
