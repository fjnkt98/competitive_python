def main():
    S = input()
    N, M = map(int, input().split())

    T = list(S)
    T[N - 1], T[M - 1] = T[M - 1], T[N - 1]

    print("".join(T))


if __name__ == "__main__":
    main()
