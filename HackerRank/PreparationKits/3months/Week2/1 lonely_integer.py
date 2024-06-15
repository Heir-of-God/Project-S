import os


def lonelyinteger(arr):
    res: int = 0
    for n in arr:
        res ^= n
    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    fptr.write(str(result) + "\n")
    fptr.close()
