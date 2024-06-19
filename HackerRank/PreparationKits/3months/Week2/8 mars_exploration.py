import os


def marsExploration(s) -> int:
    sos = "SOS"
    cur_ind = 0
    res = 0

    for char in s:
        if sos[cur_ind] != char:
            res += 1
        cur_ind += 1
        if cur_ind == len(sos):
            cur_ind = 0

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + "\n")
    fptr.close()
