import itertools
import sys

sys.setrecursionlimit(1000000)


def factorize(N: int) -> dict[int, int]:
    result = {}

    i: int = 2
    while i * i <= N:
        if N % i == 0:
            exp: int = 0

            while N % i == 0:
                N //= i
                exp += 1

            result[i] = exp
        i += 1

    if N != 1:
        result[N] = 1

    return result


def main() -> None:
    N: int = int(input())
    A: list[int] = sorted(int(v.strip()) for v in input().split())
    F = [factorize(a) for a in A]
    keys = set(itertools.chain.from_iterable([f.keys() for f in F]))
    counter = {k: 0 for k in keys}
    min_2 = 9999999999
    min_3 = 9999999999
    for f in F:
        min_2 = min(min_2, f.get(2, 0))
        min_3 = min(min_3, f.get(3, 0))
        for k in f.keys():
            counter[k] += 1

    for k, v in counter.items():
        if k not in [2, 3] and v != N:
            print(-1)
            return

    answer = 0
    for f in F:
        answer += f.get(2, 0) - min_2
        answer += f.get(3, 0) - min_3

    print(answer)


if __name__ == "__main__":
    main()
