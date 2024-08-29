n = int(input())
arr = [(int(i), ind) for ind, i in enumerate(input().split())]
arr.sort(reverse=True)
res = n

for ind, val in enumerate(arr):
    res += ind * val[0]

print(res)
print(" ".join([str(i[1] + 1) for i in arr]))
