from typing import List


def main():
    N = int(input())
    R: List[int] = [int(input()) for i in range(N)]

    answer: int = -1e10
    minimum: int = 1e10

    for r in R:
        answer = max(answer, r - minimum)
        minimum = min(minimum, r)

    print(answer)


if __name__ == "__main__":
    main()
