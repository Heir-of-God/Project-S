import os


def caesarCipher(s: str, k: int) -> str:
    k %= 26
    res = ""
    for char in s:
        if char.isalpha():
            new_code = (
                (ord(char) - ord("a") + k) % 26 + ord("a")
                if char.islower()
                else (ord(char) - ord("A") + k) % 26 + ord("A")
            )
            res += chr(new_code)
        else:
            res += char

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + "\n")
    fptr.close()
