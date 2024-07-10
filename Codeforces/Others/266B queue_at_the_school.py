n, time = [int(i) for i in input().split()]
childrens = list(input())

for _ in range(time):
    was = childrens[:]
    for ind in range(1, n):
        if was[ind - 1] == "B" and was[ind] == "G":
            childrens[ind - 1], childrens[ind] = childrens[ind], childrens[ind - 1]

print("".join(childrens))
