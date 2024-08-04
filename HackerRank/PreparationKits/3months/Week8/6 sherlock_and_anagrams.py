import os


def sherlockAndAnagrams(s: str) -> int:
    n: int = len(s)
    count: dict[str, int] = {}

    for start_ind in range(n):
        for end_ind in range(start_ind, n, 1):
            substring = "".join(sorted(s[start_ind : end_ind + 1]))
            if substring not in count:
                count[substring] = 0
            count[substring] += 1

    res = 0
    for val in count.values():
        res += (val * (val - 1)) // 2
    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + "\n")
    fptr.close()
