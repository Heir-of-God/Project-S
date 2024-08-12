t = int(input())

for _ in range(t):
    s = input()
    print("YES" if s in ["abc", "cba", "bac", "acb"] else "NO")
