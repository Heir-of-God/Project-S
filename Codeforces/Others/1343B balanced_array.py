t = int(input())

for _ in range(t):
    n = int(input())
    if n % 4 != 0:
        print("NO")
        continue
    even_part = []
    odd_part = []

    cur_center = 3
    for _ in range(n // 4):
        even_part.append(cur_center - 1)
        even_part.append(cur_center + 1)
        odd_part.append(cur_center - 2)
        odd_part.append(cur_center + 2)
        cur_center += 6

    print("YES")
    print(" ".join([str(i) for i in even_part + odd_part]))
