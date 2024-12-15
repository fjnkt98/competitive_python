import itertools


def main() -> None:
    N, K = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    answer = 0
    for i, j in itertools.product(range(101), range(101)):
        count = 0
        for a, b in zip(A, B):
            if i <= a <= i + K and j <= b <= j + K:
                count += 1
        answer = max(answer, count)
    print(answer)


if __name__ == "__main__":
    main()
