t = int(input())

for _ in range(t):
    rows = [input() for _ in range(3)]
    for row in rows:
        if "?" in row:
            print("A" if ("B" in row and "C" in row) else "B" if ("C" in row) else "C")
