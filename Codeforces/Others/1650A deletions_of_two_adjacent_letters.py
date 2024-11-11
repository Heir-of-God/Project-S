t = int(input())

for _ in range(t):
    s = input()
    c = input()

    found = False
    for ind in range(0, len(s), 2):
        if s[ind] == c:
            print("YES")
            found = True
            break

    if not found:
        print("NO")
