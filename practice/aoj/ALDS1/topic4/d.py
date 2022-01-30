from typing import List


def main():
    N, K = map(int, input().split())
    W: List[int] = [int(input()) for i in range(N)]

    left: int = 0
    right: int = 1000000000000
    while right - left > 1:
        mid: int = (left + right) // 2

        truck: int = 1
        load: int = 0

        ok: bool = True

        for w in W:
            if mid < w:
                ok = False
                break

            if load + w > mid:
                truck += 1
                load = 0

            load += w

        if truck > K or load > mid:
            ok = False

        if ok:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()
