n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
dragons = int(input())
res = 0

for dragon in range(1, dragons + 1, 1):
    if 0 in (dragon % n1, dragon % n2, dragon % n3, dragon % n4):
        res += 1

print(res)
