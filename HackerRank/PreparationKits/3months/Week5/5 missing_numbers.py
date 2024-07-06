import os


def missingNumbers(arr: list[int], brr: list[int]) -> list[int]:
    counting: list[int] = [0 for _ in range(101)]
    mn: int = min(brr)
    res: list[int] = []

    for num in brr:
        counting[num - mn] += 1

    for num in arr:
        counting[num - mn] -= 1

    for num_ind in range(101):
        num: int = num_ind + mn
        if counting[num_ind] > 0:
            res.append(num)

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
