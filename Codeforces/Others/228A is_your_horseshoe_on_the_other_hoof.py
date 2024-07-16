has = [int(i) for i in input().split()]
res = 0
seen = set()

for i in has:
    if i not in seen:
        seen.add(i)
    else:
        res += 1

print(res)
