import itertools


def main():
    N = int(input())
    S = input()

    count: int = 0
    for (i, j) in itertools.combinations(range(N), 2):
        if S[i] == S[j]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
