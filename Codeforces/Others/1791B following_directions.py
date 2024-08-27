t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    x, y = 0, 0

    flag = False
    for char in s:
        if char == "L":
            x -= 1
        elif char == "R":
            x += 1
        elif char == "U":
            y += 1
        elif char == "D":
            y -= 1

        if x == 1 and y == 1:
            flag = True
            break

    print("YES" if flag else "NO")
