_ = int(input())
events = [int(i) for i in input().split()]
res = 0
cur_officers = 0

for event in events:
    if event == -1:
        if cur_officers:
            cur_officers -= 1
        else:
            res += 1
    else:
        cur_officers += event

print(res)
