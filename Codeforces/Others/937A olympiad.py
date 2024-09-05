n = int(input())
arr = [int(i) for i in input().split()]
seen = set()

for n in arr:
    if n not in seen:
        seen.add(n)

print(len(seen) - (1 if 0 in seen else 0))
