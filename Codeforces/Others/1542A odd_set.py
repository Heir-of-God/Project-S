t = int(input())

for _ in range(t):
    pairs = int(input())
    arr = [int(i) for i in input().split()]

    odd_count = 0
    even_count = 0

    for el in arr:
        if el & 1 == 1:
            odd_count += 1
        else:
            even_count += 1

    print("Yes" if even_count == odd_count else "No")
