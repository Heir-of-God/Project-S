n = int(input())
arr = [int(i) for i in input().split()]

prog = []
math = []
pe = []

for ind, val in enumerate(arr, 1):
    if val == 1:
        prog.append(ind)
    elif val == 2:
        math.append(ind)
    else:
        pe.append(ind)

mn = min(len(prog), len(math), len(pe))
print(mn)
for ind in range(mn):
    print(f"{prog[ind]} {math[ind]} {pe[ind]}")
