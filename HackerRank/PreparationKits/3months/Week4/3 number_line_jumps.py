import os


def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    if v1 == v2:
        return "NO"
    n = (x2 - x1) / (v1 - v2)
    return "YES" if n > 0 and n == int(n) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()
