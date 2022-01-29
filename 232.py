import itertools


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count: int = 0
    for a, b in itertools.product(A, B):
        if a + b == K:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
