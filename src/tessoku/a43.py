def main() -> None:
    N, L = map(int, input().split())
    A, B = map(list, zip(*[input().split() for i in range(N)]))
    A = [int(a) for a in A]

    E = [a for a, b in zip(A, B) if b == "E"]
    W = [a for a, b in zip(A, B) if b == "W"]

    if E:
        e = max([L - e for e in E])
    else:
        e = 0

    if W:
        w = max([w for w in W])
    else:
        w = 0

    print(max(e, w))


if __name__ == "__main__":
    main()
