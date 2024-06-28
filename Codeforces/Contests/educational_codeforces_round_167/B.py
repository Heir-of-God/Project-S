n = int(input())


def calculate_max_subsequence(ss, sstring):
    res = 0
    l: int = len(ss)

    for start_ind in range(l):
        cur_n = 0
        cur_ind: int = start_ind
        for char in sstring:
            if cur_ind == l:
                break
            if char == ss[cur_ind]:
                cur_n += 1
                cur_ind += 1
        res: int = max(res, cur_n)
    return res


for _ in range(n):
    substring: str = input()
    subsequence: str = input()
    dod: int = calculate_max_subsequence(subsequence, substring)
    print(len(substring) + (len(subsequence) - dod))
