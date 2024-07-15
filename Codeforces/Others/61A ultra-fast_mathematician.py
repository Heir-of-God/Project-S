n1 = input()
n2 = input()
length = len(n1)
res = ""

for ind in range(length):
    dig1 = n1[ind]
    dig2 = n2[ind]

    res += str(int(dig1 != dig2))

print(res)
