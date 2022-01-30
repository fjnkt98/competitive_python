from typing import List, Tuple, Deque
import collections


def main():
    S: str = input()

    slopes: Deque[int] = collections.deque()
    partial_ponds: Deque[Tuple(int, int)] = collections.deque()

    sum_area: int = 0

    for i, s in enumerate(list(S)):
        if s == "\\":
            slopes.append(i)

        if s == "/" and slopes:
            local_area: int = i - slopes[-1]

            sum_area += local_area

            while partial_ponds and slopes[-1] < partial_ponds[-1][0]:
                local_area += partial_ponds[-1][1]
                partial_ponds.pop()

            partial_ponds.append((slopes.pop(), local_area))

    result: List[int] = [p[1] for p in list(partial_ponds)]
    print(sum_area)
    if result:
        print(len(partial_ponds), " ".join(map(str, result)))
    else:
        print(len(partial_ponds))


if __name__ == "__main__":
    main()
