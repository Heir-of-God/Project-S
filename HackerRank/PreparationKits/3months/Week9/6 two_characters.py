import os


def alternate(s: str) -> int:
    chars: list[str] = list(set(list(s)))
    cur_res = 0

    def check_answer(first, second) -> int:
        local_res = 0
        prev: str = ""

        for char in s:
            if char in (first, second):
                if prev != char:
                    local_res += 1
                    prev = char
                else:
                    return 0

        return local_res

    for first_char_ind in range(0, len(chars), 1):
        for second_char_ind in range(first_char_ind + 1, len(chars), 1):
            first: str = chars[first_char_ind]
            second: str = chars[second_char_ind]
            cur_res: int = max(cur_res, check_answer(first, second))

    return cur_res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    l = int(input().strip())
    s = input()
    result = alternate(s)
    fptr.write(str(result) + "\n")
    fptr.close()
