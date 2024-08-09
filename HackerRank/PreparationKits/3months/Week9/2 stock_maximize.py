import os


def stockmax(prices: list[int]) -> int:
    if not prices:
        return 0
    mx: int = max(prices)
    mx_ind: int = prices.index(mx)
    buy: list[int] = prices[:mx_ind]

    return (prices[mx_ind] * len(buy)) - sum(buy) + stockmax(prices[mx_ind + 1 :])


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        prices = list(map(int, input().rstrip().split()))
        result = stockmax(prices)
        fptr.write(str(result) + "\n")
    fptr.close()
