t = int(input())

for _ in range(t):
    n = int(input())
    made = [int(i) for i in input().split()]
    moves = [input().split()[1] for _ in range(n)]
    res = []

    for i, m in enumerate(moves):
        new = made[i]
        for char in m:
            new += -1 if char == "U" else 1
            if new == -1:
                new = 9
            elif new == 10:
                new = 0
        res.append(new)

    print(*res)
