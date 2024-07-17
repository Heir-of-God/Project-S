n = int(input())
f = n // 2
res = ["I hate", "I love"] * f
if n & 1 == 1:
    res += ["I hate"]
res = " that ".join(res)
res += " it"

print(res)
