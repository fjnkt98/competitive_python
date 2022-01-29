from typing import List


def main():
    N = int(input())
    S: List[str] = [input() for i in range(N)]

    count: int = 0
    for s in S:
        if s == s[::-1]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
