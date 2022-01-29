def main():
    N = int(input())
    S: list[str] = ["" for i in range(N)]

    answer: list[str] = []

    for i in range(N):
        S = input()

        answer.append(S[0])

    print("".join(answer))


if __name__ == "__main__":
    main()
