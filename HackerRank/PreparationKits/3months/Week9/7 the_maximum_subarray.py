import os


def maxSubarray(arr: list[int]) -> list[int]:
    subseq_sum = 0
    mx_subarr = 0
    subarr_sum = 0
    arr.append(-float("inf"))

    for n in arr:
        if n > 0:
            subseq_sum += n
        else:
            mx_subarr: int = max(mx_subarr, subarr_sum)

        if subarr_sum + n < 0:
            subarr_sum: int = -n
        subarr_sum += n

    return [mx_subarr if mx_subarr != 0 else max(arr), subseq_sum if subseq_sum != 0 else max(arr)]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = maxSubarray(arr)
        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")
    fptr.close()
