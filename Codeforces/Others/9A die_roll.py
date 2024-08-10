a1, a2 = [int(i) for i in input().split()]
mx = max(a1, a2)

if mx == 1:
    print("1/1")
elif mx == 3:
    print("2/3")
elif mx == 4:
    print("1/2")
elif mx == 5:
    print("1/3")
else:
    print(f"{6 - mx + 1}/6")
