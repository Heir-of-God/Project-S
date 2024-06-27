import os


def get_number_of_digits(num):
    res = 0
    while num // (10**res) != 0:
        res += 1
    return res


def separateNumbers(s: str) -> None:
    n: int = len(s)
    for end_ind in range(len(s) // 2):
        first_num: str = int(s[: end_ind + 1])
        cur_start_ind: int = end_ind + 1
        next_num_search: int = first_num + 1
        flag = True
        while cur_start_ind < n:
            digits: int = get_number_of_digits(next_num_search)
            next_part = int(s[cur_start_ind : cur_start_ind + digits])
            if next_part != next_num_search:
                flag = False
                break
            next_num_search += 1
            cur_start_ind = cur_start_ind + digits
        if flag:
            print(f"YES {first_num}")
            return
    print("NO")


if __name__ == "__main__":
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)
