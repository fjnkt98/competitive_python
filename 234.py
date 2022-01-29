import math


def is_prime(x: int) -> bool:
    if x == 1:
        return False

    for i in range(2, math.trunc(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def main():
    N = int(input())
    A = list(map(int, input().split()))

    count: int = 0
    for a in A:
        if is_prime(a):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
