import os


def superDigit(n: str, k: int) -> int:
    res = 0
    for char in n:
        res += int(char)
    res *= k
    if res // 10 == 0:
        return res
    return superDigit(str(res), 1)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + "\n")
    fptr.close()
