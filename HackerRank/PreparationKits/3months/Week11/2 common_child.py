import os


def commonChild(s1: str, s2: str) -> int:
    l1: int = len(s1)
    l2: int = len(s2)
    dp: list[list[int]] = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    for number_of_elems1 in range(1, l1 + 1):
        ind1: int = number_of_elems1 - 1
        for number_of_elems2 in range(1, l2 + 1):
            ind2: int = number_of_elems2 - 1
            dp[number_of_elems1][number_of_elems2] = max(
                dp[number_of_elems1 - 1][number_of_elems2], dp[number_of_elems1][number_of_elems2 - 1]
            )  # maximum here - maximum from ignoring last char in s1 or s2

            if s1[ind1] == s2[ind2]:
                dp[number_of_elems1][number_of_elems2] = max(
                    dp[number_of_elems1][number_of_elems2], dp[number_of_elems1 - 1][number_of_elems2 - 1] + 1
                )  # if you can add this character to subsequence - check maximum for previous state

    # dp[i][j] means maximum length of common subsequence if you use first i characters from s1 and first j characters from s2

    return dp[l1][l2]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    fptr.write(str(result) + "\n")
    fptr.close()
