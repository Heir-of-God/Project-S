n = int(input())
line = [int(i) for i in input().split()]

mx = max(line)
mn = min(line)
mx_steps = -1
mn_steps = -1

for ind, el in enumerate(line):
    if el == mx and mx_steps == -1:
        mx_steps = ind
    if el == mn:
        mn_steps = n - 1 - ind - (mx_steps == -1)

print(mx_steps + mn_steps)
