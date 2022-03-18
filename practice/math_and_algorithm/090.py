from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline

answer: int = 0


def f(S: str) -> int:
    result: int = 1
    for s in list(S):
        result *= int(s)

    return result


def dfs(digit: int, limit: int, S: str, N: int, B: int) -> None:
    global answer

    if digit == 0:
        m = f(S) + B
        if m <= N:
            if S == "".join(sorted(str(m), reverse=True)):
                answer += 1

        return

    for i in range(limit, 0, -1):
        dfs(digit - 1, i, S + str(i), N, B)


def main():
    global answer
    N, B = map(int, input().split())

    for i in range(1, 12):
        dfs(i, 9, "", N, B)

    if ("0" in str(B)) and N >= B:
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
