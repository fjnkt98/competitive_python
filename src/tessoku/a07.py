import itertools


def main() -> None:
    D: int = int(input())
    N: int = int(input())
    L, R = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    C = [0] * (D + 2)
    for l, r in zip(L, R):
        C[l] += 1
        C[r + 1] -= 1

    C = list(itertools.accumulate(C))[1:-1]

    print(*C, sep="\n")


if __name__ == "__main__":
    main()
