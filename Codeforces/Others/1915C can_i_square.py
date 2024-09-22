t = int(input())

for _ in range(t):
    _ = input()
    arr = [int(i) for i in input().split()]
    sm = sum(arr)
    print("YES" if sm**0.5 == int(sm**0.5) else "NO")
