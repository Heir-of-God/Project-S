s = input()
qs = s.count("Q")
left_q = 0
res = 0

for char in s:
    if char == "Q":
        left_q += 1
    elif char == "A":
        res += left_q * (qs - left_q)

print(res)
