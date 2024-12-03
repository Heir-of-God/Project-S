t = int(input())

for _ in range(t):
    n = int(input())
    print("Kosuke" if n & 1 == 1 else "Sakurako")
