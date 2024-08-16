t = int(input())
cf = "codeforces"


for _ in range(t):
    s = input()
    res = 0
    for ind in range(10):
        res += cf[ind] != s[ind]

    print(res)
