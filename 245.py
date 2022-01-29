import itertools


def main():
    L, R = map(int, input().split())

    count: int = 0
    for (i, j) in itertools.combinations(range(L, R + 1), 2):
        if i % 10 == j % 10:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
