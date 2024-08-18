import operator


def main() -> None:
    N: int = int(input())
    L, R = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    D = sorted([(l, r) for l, r in zip(L, R)], key=operator.itemgetter(1))

    count = 0
    last = 0
    for l, r in D:
        if l < last:
            continue
        count += 1
        last = r

    print(count)


if __name__ == "__main__":
    main()
