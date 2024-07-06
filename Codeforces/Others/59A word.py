w = input()
c_lower = 0
c_upper = 0

for char in w:
    if ord(char) >= ord("a"):
        c_lower += 1
    else:
        c_upper += 1

if c_lower >= c_upper:
    print(w.lower())
else:
    print(w.upper())
