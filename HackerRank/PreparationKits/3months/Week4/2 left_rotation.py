import os


def rotateLeft(d: int, arr: list[int]):
    n: int = len(arr)
    d %= n
    for _ in range(d):
        arr.append(arr.pop(0))
    return arr


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
