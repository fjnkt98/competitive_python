import itertools


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    count: int = 0
    for (a, b) in itertools.combinations(A, 2):
        if a + b <= K:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
