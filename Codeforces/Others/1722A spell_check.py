t = int(input())
tr = {}
for char in "Timur":
    tr[char] = 1

for _ in range(t):
    n = int(input())
    s = input()
    c = {}
    for char in s:
        if char not in c:
            c[char] = 0
        c[char] += 1

    print("YES" if c == tr else "NO")
