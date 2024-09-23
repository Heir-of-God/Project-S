t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    even = 0
    for num in a:
        even += num if num & 1 == 0 else 0

    print("YES" if even > sum(a) - even else "NO")
