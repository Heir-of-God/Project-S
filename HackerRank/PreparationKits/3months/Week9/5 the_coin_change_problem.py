import os


def getWays(amount: int, coins: list[int]) -> int:
    dp: list[int] = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for coin in coins:
        for summ in range(coin, amount + 1):
            dp[summ] += dp[summ - coin]

    return dp[amount]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, c)
    fptr.write(str(ways) + "\n")
    fptr.close()
