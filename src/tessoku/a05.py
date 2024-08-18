import itertools


def main() -> None:
    N, K = map(int, input().split())

    count = 0
    for i, j in itertools.product(range(1, N + 1), repeat=2):
        if 1 <= K - i - j <= N:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
