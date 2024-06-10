def miniMaxSum(arr) -> None:
    mx = mn = sum(arr)
    mx -= min(arr)
    mn -= max(arr)
    print(f"{mn} {mx}")


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
