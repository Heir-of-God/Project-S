t = int(input())

for _ in range(t):
    n = int(input())
    arr = [abs(int(i)) for i in input().split()]

    print(sum(arr))
