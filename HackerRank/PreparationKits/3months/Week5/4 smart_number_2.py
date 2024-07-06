import math


def is_smart_number(num) -> bool:
    val = int(math.sqrt(num))
    if num == val**2:
        return True
    return False


for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
