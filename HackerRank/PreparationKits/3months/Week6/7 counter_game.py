import os
import math


def counterGame(n: int) -> str:
    res = 0

    while n != 1:

        exponent = math.log2(n)
        if exponent.is_integer():
            res += int(exponent)
            break
        n = n - 2 ** int(exponent)
        res += 1

    return "Louise" if res & 1 == 1 else "Richard"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = counterGame(n)
        fptr.write(result + "\n")
    fptr.close()
