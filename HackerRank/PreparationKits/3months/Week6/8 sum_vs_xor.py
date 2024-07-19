import os


def sumXor(n: int) -> int:
    print(bin(n)[2:].count("0"))
    return 2 ** bin(n)[2:].count("0") if n != 0 else 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    result = sumXor(n)
    fptr.write(str(result) + "\n")
    fptr.close()
