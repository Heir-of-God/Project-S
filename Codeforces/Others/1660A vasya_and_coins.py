t = int(input())

for _ in range(t):
    a, b = [int(i) for i in input().split()]  # if a == 0 then he never can achieve any odd sum

    if a == 0:
        print(1)
    else:
        print(a + 2 * b + 1)
