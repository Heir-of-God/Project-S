import os


def equalStacks(h1: list[int], h2: list[int], h3: list[int]) -> int:
    s1: int = sum(h1)
    s2: int = sum(h2)
    s3: int = sum(h3)
    n1: int = len(h1)
    n2: int = len(h2)
    n3: int = len(h3)

    ind1 = ind2 = ind3 = 0

    while ind1 < n1 and ind2 < n2 and ind3 < n3 and 0 not in [s1, s2, s3] and not (s1 == s2 == s3):
        mx: int = max(s1, s2, s3)
        if mx == s1:
            s1 -= h1[ind1]
            ind1 += 1
        elif mx == s2:
            s2 -= h2[ind2]
            ind2 += 1
        elif mx == s3:
            s3 -= h3[ind3]
            ind3 += 1

    return min(s1, s2, s3)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result = equalStacks(h1, h2, h3)
    fptr.write(str(result) + "\n")
    fptr.close()
