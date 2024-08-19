import os


def permutationGame(arr):
    is_increasing = lambda arr: all([arr[i] < arr[i + 1] for i in range(len(arr) - 1)])

    memo = {}

    def findWinner(arr):
        tpl_arr = tuple(arr)
        if tpl_arr in memo:
            return memo[tpl_arr]

        if is_increasing(arr):
            memo[tpl_arr] = True
            return True

        for ind in range(len(arr)):
            if findWinner(arr[:ind] + arr[ind + 1 :]):
                # if found any continue from this which ends to lose
                memo[tpl_arr] = False
                return False

        # if all continues are wins
        memo[tpl_arr] = True
        return True

    return "Bob" if findWinner(arr) else "Alice"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        arr_count = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = permutationGame(arr)
        fptr.write(result + "\n")
    fptr.close()
