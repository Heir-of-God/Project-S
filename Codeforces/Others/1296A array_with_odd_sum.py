t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    odd = 0

    for num in arr:
        odd += num & 1
    even = n - odd

    print("YES" if ((odd & 1 == 0 and even and odd != 0) or odd & 1 == 1) else "NO")
