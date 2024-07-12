import os


def balancedSums(arr: list[int]) -> str:
    prefix_s = 0
    suffix_s = sum(arr)

    for el in arr:
        suffix_s -= el
        if prefix_s == suffix_s:
            return "YES"
        prefix_s += el

    return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        fptr.write(result + "\n")
    fptr.close()
