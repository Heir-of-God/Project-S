t = int(input())

for _ in range(t):
    ticket = [int(i) for i in input()]
    print("YES" if sum(ticket[:3]) == sum(ticket[3:]) else "NO")
