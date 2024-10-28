t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    found = False
    for ind in range(1, n):
        if s[ind - 1] != s[ind]:
            print("YES")
            print(s[: ind - 1] + s[ind] + s[ind - 1] + s[ind + 1 :])
            found = True
            break

    if found:
        continue
    print("NO")
