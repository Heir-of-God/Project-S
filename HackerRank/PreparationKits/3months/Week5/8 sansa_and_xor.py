import os


def sansaXor(arr: list[int]) -> int:
    n: int = len(arr)
    res = 0

    for cur_ind in range(n):
        start_choices: int = cur_ind + 1
        end_choices: int = n - cur_ind
        subarrays_count: int = start_choices * end_choices

        if subarrays_count & 1 == 1:
            res ^= arr[cur_ind]

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = sansaXor(arr)
        fptr.write(str(result) + "\n")
    fptr.close()
