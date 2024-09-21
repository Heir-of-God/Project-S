import os


def shortPalindrome(s):
    MOD = 1000000007
    # count_1[ord('x') - ord('a')] is the number of subsequences x
    count_1 = [0 for _ in range(26)]
    # count_2[ord('x') - ord('a')][ord('y') - ord('a')] is the number of ss xy
    count_2 = [[0 for _ in range(26)] for _ in range(26)]
    # count_3[ord('x') - ord('a')] is the count of all ss xaa, xbb, xcc, ...
    count_3 = [0 for _ in range(26)]

    res = 0
    for c in s:
        k = ord(c) - ord("a")

        res = (res + count_3[k]) % MOD
        for i in range(26):
            count_3[i] = (count_3[i] + count_2[i][k]) % MOD
        for j in range(26):
            count_2[j][k] = (count_2[j][k] + count_1[j]) % MOD

        count_1[k] = (count_1[k] + 1) % MOD

    return res % MOD


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = shortPalindrome(s)
    fptr.write(str(result) + "\n")
    fptr.close()
