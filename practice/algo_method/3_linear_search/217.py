def main():
    N = int(input())
    A = list(map(int, input().split()))

    answer: list[int] = [0 for i in range(9)]

    for a in A:
        answer[a - 1] += 1

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
