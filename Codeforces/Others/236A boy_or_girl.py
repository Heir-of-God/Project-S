name = input()
seen = set()
count = 0

for char in name:
    if char not in seen:
        count += 1
        seen.add(char)

if count & 1 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
