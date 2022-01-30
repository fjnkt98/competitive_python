from typing import List


def main():
    N = int(input())
    S = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))

    count: int = 0
    for t in T:
        if t in S:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
