weight: int = int(input())
print("YES" if weight & 1 == 0 and weight != 2 else "NO")
