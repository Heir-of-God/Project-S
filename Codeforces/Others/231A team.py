n = int(input())
res = 0

for _ in range(n):
    line = input()
    res += line.count("1") >= 2

print(res)
