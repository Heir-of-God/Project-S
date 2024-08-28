import os


def highestValuePalindrome(s: str, n: int, ops: int) -> str:
    s = list(s)
    changes = 0
    changes_inds = set()

    for ind in range(n // 2):
        reversed_ind: int = n - ind - 1
        if s[ind] != s[reversed_ind]:
            changes += 1
            mx = max((s[ind], s[reversed_ind]))
            s[ind] = mx
            s[reversed_ind] = mx
            changes_inds.add(ind)

    if changes > ops:
        return "-1"

    changes: int = ops - changes
    cur_ind = 0
    while cur_ind < n // 2 and changes != 0:
        if s[cur_ind] != "9" and (changes >= 2 or cur_ind in changes_inds):
            if cur_ind in changes_inds:
                changes += 1
            changes -= 2
            s[cur_ind] = "9"
            s[n - cur_ind - 1] = "9"

        cur_ind += 1

    if n & 1 == 1 and changes > 0:
        s[n // 2] = "9"

    return "".join(s)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input()
    result = highestValuePalindrome(s, n, k)
    fptr.write(result + "\n")
    fptr.close()
