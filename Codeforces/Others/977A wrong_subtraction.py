num, op = input().split()
num = int(num)
op = int(op)

while op != 0:
    last_dig = num % 10
    cur_n = min(last_dig + 1, op)
    if last_dig + 1 == cur_n:
        num //= 10
    else:
        num -= cur_n
    op -= cur_n

print(num)
