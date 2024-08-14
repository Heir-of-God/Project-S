t = int(input())

for _ in range(t):
    n = input().strip()
    res = "YES"
    if len(n) < 3 or n[:2] != "10" or n[2] == "0" or (len(n) == 3 and n[2] == "1"):
        res = "NO"
    print(res)
