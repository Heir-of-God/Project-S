n = int(input())
s = input()
count = 0
res = 0

for char in s:
    if char == "x":
        if count == 2:
            res += 1
        else:
            count += 1
    else:
        count = 0

print(res)
