red, blue = [int(i) for i in input().split()]
res1 = min(red, blue)
red -= res1
blue -= res1

res2 = 0
res2 += red // 2
res2 += blue // 2

print(res1, res2)
