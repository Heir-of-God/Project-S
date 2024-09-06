import os


def beadOrnaments(b: list[int]) -> int:
    sumColor = 0
    intercolor = 1
    for color in b:
        intercolor *= color ** (color - 1)
        sumColor += color
    intercolor *= sumColor ** (len(b) - 2)
    return int(intercolor % (10**9 + 7))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        b_count = int(input().strip())
        b = list(map(int, input().rstrip().split()))
        result = beadOrnaments(b)
        fptr.write(str(result) + "\n")
    fptr.close()
