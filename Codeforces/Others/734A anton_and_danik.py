n = int(input())
s = input()

a = 0
d = 0

for char in s:
    if char == "A":
        a += 1
    else:
        d += 1

print("Anton" if a > d else "Danik" if d > a else "Friendship")
