t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    first_b = -1
    last_b = -1

    for ind, char in enumerate(s):
        if char == "B":
            if first_b == -1:
                first_b = ind
            last_b = ind

    if first_b == -1:
        print(0)
    else:
        print(last_b - first_b + 1)
