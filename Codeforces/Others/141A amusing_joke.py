counter = {}
str1 = input()
str2 = input()

for char in str1:
    if char not in counter:
        counter[char] = 0
    counter[char] += 1

for char in str2:
    if char not in counter:
        counter[char] = 0
    counter[char] += 1

res = "YES"
pile = input()
for char in pile:
    if char not in counter or counter[char] == 0:
        res = "NO"
        break
    counter[char] -= 1

for val in counter.values():
    if val != 0:
        res = "NO"
        break

print(res)
