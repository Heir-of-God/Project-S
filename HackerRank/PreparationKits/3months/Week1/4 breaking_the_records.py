import os


def breakingRecords(scores: list[int]) -> list[int]:
    mx_changes = 0
    mn_changes = 0
    cur_mx: int = scores[0]
    cur_mn: int = scores[0]

    for score in scores:
        if score > cur_mx:
            mx_changes += 1
            cur_mx = score
        elif score < cur_mn:
            mn_changes += 1
            cur_mn = score

    return [mx_changes, mn_changes]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
