from typing import List, Deque, Tuple
import collections


def main():
    N, Q = map(int, input().split())
    S: List[str] = [input().split() for i in range(N)]

    queue: Deque[Tuple[str, int]] = collections.deque([(s[0], int(s[1])) for s in S])

    current_time: int = 0
    answer: List[Tuple[str, int]] = []
    while queue:
        task: Tuple[str, int] = queue.popleft()
        if task[1] <= Q:
            current_time += task[1]
            answer.append((task[0], current_time))
        else:
            current_time += Q
            queue.append((task[0], task[1] - Q))

    for a in answer:
        print(f"{a[0]} {a[1]}")


if __name__ == "__main__":
    main()
