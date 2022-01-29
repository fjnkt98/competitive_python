def main():
    N = int(input())

    answer: int = 0
    for i in range(N):
        S = input()
        answer += len(S)

    print(answer)


if __name__ == "__main__":
    main()
