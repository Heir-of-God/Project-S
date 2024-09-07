t = int(input())

for _ in range(t):
    n = int(input())
    arr = [input() for _ in range(n)]

    square = False
    flag = False
    for i in range(n):
        if flag:
            break
        for j in range(n):
            if arr[i][j] == "1":
                if arr[i + 1][j] == "1" and arr[i][j + 1] == "1":
                    square = True
                flag = True
                break

    print("SQUARE" if square else "TRIANGLE")
