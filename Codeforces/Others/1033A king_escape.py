n = int(input())
ax, ay = [int(i) for i in input().split()]
bx, by = [int(i) for i in input().split()]
cx, cy = [int(i) for i in input().split()]

relativex, relativey = bx - ax, by - ay
realtivex2, relativey2 = bx - cx, by - cy

flag = True
if (relativex > 0) == (realtivex2 > 0) and abs(relativex) < abs(realtivex2):
    flag = False
if (relativey > 0) == (relativey2 > 0) and abs(relativey) < abs(relativey2):
    flag = False

print("YES" if flag else "NO")
