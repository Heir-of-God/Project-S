def plusMinus(arr) -> None:
    n: int = len(arr)
    pos: int = 0
    neg: int = 0
    for el in arr:
        if el > 0:
            pos += 1
        elif el < 0:
            neg += 1
    zer: int = n - pos - neg
    print(round(pos / n, 6))
    print(round(neg / n, 6))
    print(round(zer / n, 6))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
