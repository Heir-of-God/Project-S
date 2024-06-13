import os


def divisibleSumPairs(n, k, arr) -> int:
    arr: list[int] = [num % k for num in arr]
    count: list[int] = [0 for _ in range(k)]
    res = 0

    for num_ind in range(len(arr) - 1, -1, -1):
        to_add: int = (k - arr[num_ind]) % k
        res += count[to_add]
        count[arr[num_ind]] += 1

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    fptr.write(str(result) + "\n")
    fptr.close()
