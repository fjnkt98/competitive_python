from typing import List, Tuple
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N = int(input())
    S: List[List[str]] = [input().split() for i in range(N)]

    task: List[Tuple[int, int]] = [(int(s[1]), int(s[0])) for s in S]

    task.sort()

    last_endpoint: int = task[0][0]
    answer: int = 1
    for i in range(1, N):
        if task[i][1] < last_endpoint:
            continue
        last_endpoint = task[i][0]
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
