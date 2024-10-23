pi = "3141592653589793238462643383279"

t = int(input())

for _ in range(t):
    s = input()
    ind = 0

    while ind < len(s) and s[ind] == pi[ind]:
        ind += 1

    print(ind)
