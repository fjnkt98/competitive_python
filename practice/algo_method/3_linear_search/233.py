import itertools


def main():
    X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    count: int = 0
    for (a, b, c) in itertools.product(A, B, C):
        if a + b == c:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
