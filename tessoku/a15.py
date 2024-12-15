def compress(A: list[int]) -> list[int]:
    X: list[int] = sorted(set(A))
    D: dict[int, int] = {x: i for i, x in enumerate(X)}
    return [D[a] for a in A]


def main() -> None:
    _: int = int(input())
    A: list[int] = [int(v.strip()) for v in input().split()]

    C = compress(A)
    print(*map(lambda x: x + 1, C))


if __name__ == "__main__":
    main()
