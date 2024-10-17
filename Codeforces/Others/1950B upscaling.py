t = int(input())

for _ in range(t):
    n = int(input())

    first_line = ""
    second_line = ""

    for _ in range(n):
        first_line += "#" * 2 if not first_line or first_line[-1] == "." else "." * 2
        second_line += "." * 2 if not second_line or second_line[-1] == "#" else "#" * 2

    cur = first_line
    for _ in range(n):
        print(cur)
        print(cur)
        cur = second_line if cur == first_line else first_line
