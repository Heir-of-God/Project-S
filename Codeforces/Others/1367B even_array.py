t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    even_outplace = 0
    odd_outplace = 0

    for ind in range(n):
        el = arr[ind]
        if ind & 1 == 1:
            if el & 1 != 1:
                odd_outplace += 1
        else:
            if el & 1 != 0:
                even_outplace += 1

    print(odd_outplace if odd_outplace == even_outplace else -1)
