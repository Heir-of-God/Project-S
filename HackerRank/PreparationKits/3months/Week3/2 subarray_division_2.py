import os


def birthday(s, d, m) -> int:
    n: int = len(s)
    res: int = 0
    cur_sum: int = 0
    left: int = 0

    for right in range(n):
        cur_sum += s[right]
        while cur_sum > d:
            cur_sum -= s[left]
            left += 1
        res += cur_sum == d and right - left + 1 == m

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + "\n")
    fptr.close()
