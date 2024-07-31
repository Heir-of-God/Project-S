t = int(input())


for _ in range(t):
    a, b, c = [int(i) for i in input().split()]
    print("YES" if a + b == c or a + c == b or b + c == a else "NO")
