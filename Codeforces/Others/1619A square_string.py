t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    res = "YES"
    if n & 1 == 1 or s[: n // 2] != s[n // 2 :]:
        res = "NO"

    print(res)
