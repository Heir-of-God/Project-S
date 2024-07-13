import os


def misereNim(s: list[int]) -> int:
    total_sum = sum(s)
    if total_sum == len(s):
        return "First" if len(s) % 2 == 0 else "Second"

    nim_sum = 0
    for num in s:
        nim_sum ^= num

    return "Second" if nim_sum == 0 else "First"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        s = list(map(int, input().rstrip().split()))
        result = misereNim(s)
        fptr.write(result + "\n")

    fptr.close()
