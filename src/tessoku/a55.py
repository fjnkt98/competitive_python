from sortedcontainers import SortedSet


def main() -> None:
    Q: int = int(input())
    S = SortedSet([])

    for _ in range(Q):
        line = input().split()

        x = int(line[1])
        match line[0]:
            case "1":
                S.add(x)
            case "2":
                S.remove(x)
            case "3":
                i = S.bisect_left(x)
                if i == len(S):
                    print(-1)
                else:
                    print(S[i])


if __name__ == "__main__":
    main()
