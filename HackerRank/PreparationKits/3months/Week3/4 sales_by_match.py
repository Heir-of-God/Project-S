import os


def sockMerchant(n: int, arr: list[int]) -> int:
    seen = set()
    res = 0

    for sock in arr:
        if sock in seen:
            seen.remove(sock)
            res += 1
        else:
            seen.add(sock)

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + "\n")
    fptr.close()
