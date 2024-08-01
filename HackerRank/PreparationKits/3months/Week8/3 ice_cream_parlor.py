import os


def icecreamParlor(money: int, prices: list[int]) -> list[int]:
    seen = {}  # num -> index

    for ind, num in enumerate(prices):
        if money - num in seen:
            return [seen[money - num] + 1, ind + 1]
        seen[num] = ind

    return -1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")
    fptr.close()
