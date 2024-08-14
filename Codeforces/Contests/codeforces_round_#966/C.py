t = int(input())


def check(temp, s):
    matching = {}
    if len(temp) != len(s):
        return "NO"

    for ind, char in enumerate(s):
        el = temp[ind]
        if el in matching and matching[el] != char or char in matching and matching[char] != el:
            return "NO"
        matching[char] = el
        matching[el] = char

    return "YES"


for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    n_s = int(input())
    strings = [input() for _ in range(n_s)]

    for string in strings:
        print(check(arr, string))
