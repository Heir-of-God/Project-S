import os


def twoArrays(k, A, B):
    n: int = len(A)
    A.sort()
    B.sort(reverse=True)

    for ind in range(n):
        if A[ind] + B[ind] < k:
            return "NO"
    return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        fptr.write(result + "\n")
    fptr.close()
