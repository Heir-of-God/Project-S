import os


def countingValleys(steps: int, path: list[str]):
    new_val = True
    res = 0
    cur_h = 0

    for char in path:
        if char == "D":
            cur_h -= 1
        elif char == "U":
            cur_h += 1

        if new_val and cur_h < 0:
            res += 1
            new_val = False
        elif not new_val and cur_h >= 0:
            new_val = True

    return res

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + "\n")
    fptr.close()
