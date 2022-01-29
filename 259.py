import itertools


def main():
    N = int(input())
    A = list(map(int, input().split()))

    count: int = 0
    for (x, y, z) in itertools.combinations(A, 3):
        if max(x, y, z) == y:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
