n1, n2, n3, n4 = [int(i) for i in input().split()]
mx = max(n1, n2, n3, n4)
print(*[mx - n for n in (n1, n2, n3, n4) if mx != n])
