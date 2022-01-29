def main():
    N, V = map(int, input().split())
    A = list(map(int, input().split()))

    answer: int = -1
    for i, a in enumerate(reversed(A), 1):
        if a == V:
            answer = N - i
            break

    print(answer)


if __name__ == "__main__":
    main()
