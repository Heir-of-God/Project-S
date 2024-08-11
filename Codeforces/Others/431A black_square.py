a = [int(i) for i in input().split()]
strings = input()
res = 0

for char in strings:
    res += a[ord(char) - ord("1")]

print(res)
