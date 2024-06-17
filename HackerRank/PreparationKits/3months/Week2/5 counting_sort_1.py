import os


def countingSort(arr: list[int]) -> list[int]:
    res: list[int] = [0 for _ in range(100)]
    for n in arr:
        res[n] += 1
    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
