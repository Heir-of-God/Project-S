n = int(input())
last = ""
res = 0

for _ in range(n):
    cur = input()
    if cur != last:
        res += 1
    last = cur

print(res)
