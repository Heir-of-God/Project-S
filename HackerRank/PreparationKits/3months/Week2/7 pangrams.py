import os


def pangrams(s) -> None:
    chars: int = 0
    seen: list[bool] = [False for _ in range(26)]

    for char in s:
        n: int = ord(char.lower())
        if char.isalpha() and not seen[n - ord("a")]:
            seen[n - ord("a")] = True
            chars += 1
            if chars == 26:
                return "pangram"

    return "not pangram"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = pangrams(s)
    fptr.write(result + "\n")
    fptr.close()
