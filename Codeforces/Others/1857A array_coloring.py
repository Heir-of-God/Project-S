t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    odd_count = 0

    for el in arr:
        if el & 1 == 1:
            odd_count += 1

    print("YES" if odd_count & 1 == 0 else "NO")
