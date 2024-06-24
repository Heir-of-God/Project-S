import os


def pageCount(n: int, p: int) -> int:
    return min(p, (n // 2) * 2 + 1 - p) // 2


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    p = int(input().strip())
    result = pageCount(n, p)
    fptr.write(str(result) + "\n")
    fptr.close()
