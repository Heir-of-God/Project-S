inp = input()
# print(inp.capitalize())
print((chr(ord(inp[0]) - 32) if ord(inp[0]) >= 92 else inp[0]) + inp[1:])
