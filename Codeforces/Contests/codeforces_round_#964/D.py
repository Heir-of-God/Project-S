t = int(input())

for _ in range(t):
    to_fill = list(input())
    target = input()

    cur_ind_fill = 0
    cur_ind_read = 0

    while cur_ind_read != len(target) and cur_ind_fill != len(to_fill):
        cur_char = target[cur_ind_read]
        while cur_ind_fill != len(to_fill) and to_fill[cur_ind_fill] not in f"{cur_char}?":
            cur_ind_fill += 1
        if cur_ind_fill == len(to_fill):
            break
        to_fill[cur_ind_fill] = cur_char
        cur_ind_fill += 1
        cur_ind_read += 1

    to_fill = "".join(to_fill)
    if "?" in to_fill:
        to_fill = to_fill.replace("?", "s")

    if cur_ind_read == len(target):
        print("YES")
        print(to_fill)
    else:
        print("NO")
