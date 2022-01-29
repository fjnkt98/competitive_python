def main():
    S = input()

    N: int = len(S)

    for i in range(N // 2):
        if S[i] != S[N - i - 1]:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
