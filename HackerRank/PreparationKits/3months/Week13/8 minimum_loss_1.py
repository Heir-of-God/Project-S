import os


def minimumLoss(prices: list[int]) -> int:
    prices = [(price, ind) for ind, price in enumerate(prices)]
    prices.sort(reverse=True)
    stack = []
    res = float("inf")

    for price, original_ind in prices:
        while stack and stack[-1][1] < original_ind:
            prev_price, prev_ind = stack.pop()
            res = min(res, prev_price - price)
        stack.append((price, original_ind))

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    price = list(map(int, input().rstrip().split()))
    result = minimumLoss(price)
    fptr.write(str(result) + "\n")
    fptr.close()
