t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    f = input()

    m01 = 0
    m10 = 0

    for i in range(n):
        if s[i] + f[i] == "01":
            m01 += 1
        elif s[i] + f[i] == "10":
            m10 += 1

    print(max(m10, m01))
