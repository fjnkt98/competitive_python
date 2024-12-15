import itertools


def main() -> None:
    N, Q = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]
    L, R = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    C = list(itertools.accumulate(A, initial=0))
    for l, r in zip(L, R):
        print(C[r] - C[l - 1])


if __name__ == "__main__":
    main()
