def main() -> None:
    N: int = int(input())
    A: list[int] = [int(v.strip()) for v in input().split()]

    S: list[tuple[int, int]] = []
    answer = [-2] * N

    for i, a in enumerate(A):
        while S:
            index, top = S[-1]
            if top > a:
                break
            else:
                S.pop()
        if S:
            answer[i] = index

        S.append((i, a))

    print(*map(lambda a: a + 1, answer))


if __name__ == "__main__":
    main()
