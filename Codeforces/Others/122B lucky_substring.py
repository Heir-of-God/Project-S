s = input()
four = 0
seven = 0

for char in s:
    if char == "4":
        four += 1
    elif char == "7":
        seven += 1

print(-1 if not four and not seven else "4" if four >= seven else "7")
