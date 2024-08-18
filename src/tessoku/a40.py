from collections import Counter


def main() -> None:
    _: int = int(input())
    A: list[int] = [int(v.strip()) for v in input().split()]

    C = Counter(A)
    answer = 0
    for _, v in C.items():
        answer += (v * (v - 1) * (v - 2)) // 6

    print(answer)


if __name__ == "__main__":
    main()
