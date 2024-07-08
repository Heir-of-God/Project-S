s = input()
t = input()
n = len(s)

cur_ind = 0

res = "YES"
while cur_ind != n:
    reverse_ind = -cur_ind - 1
    if s[cur_ind] != t[reverse_ind]:
        res = "NO"
        break
    cur_ind += 1

print(res)
