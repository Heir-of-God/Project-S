n = int(input())
laptops = [[int(i) for i in input().split()] for _ in range(n)]
outdated = [False for _ in range(n)]

for i in range(n):
    for j in range(n):
        if laptops[i][0] < laptops[j][0] and laptops[i][1] < laptops[j][1] and laptops[i][2] < laptops[j][2]:
            outdated[i] = True
            break

mn_num = -1
mn_price = float("inf")

for num, (_, _, _, price) in enumerate(laptops, 1):
    if price < mn_price and outdated[num - 1] == False:
        mn_price = price
        mn_num = num

print(mn_num)
