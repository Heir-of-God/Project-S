t = int(input())

for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()

    s1 = s1.replace("G", "B")
    s2 = s2.replace("G", "B")

    print("YES" if s1 == s2 else "NO")
