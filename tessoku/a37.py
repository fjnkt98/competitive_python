def main() -> None:
    N, M, B = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]
    C: list[int] = [int(v.strip()) for v in input().split()]

    answer = (
        sum(map(lambda a: a * M, A)) + sum(map(lambda c: c * N, C)) + B * N * M
    )
    print(answer)


if __name__ == "__main__":
    main()
