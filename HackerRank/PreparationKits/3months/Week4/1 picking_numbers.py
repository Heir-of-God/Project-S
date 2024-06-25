import os


def pickingNumbers(a: list[int]) -> int:
    res: int = 0
    a.sort()

    for i in range(len(a)):
        min_el: int = a[i]
        next_ind: int = i + 1

        while (next_ind < len(a)) and (a[next_ind] - min_el < 2):
            next_ind += 1

        if res < (next_ind - i):
            res = next_ind - i

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    res = pickingNumbers(a)
    fptr.write(str(res) + "\n")
    fptr.close()
