n1 = input()
n2 = input()
length = len(n1)
res = 0

for ind in range(length):
    dig1 = n1[ind]
    dig2 = n2[ind]

    res = res * 10 + (dig1 != dig2)

print(res)
