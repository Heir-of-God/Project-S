import os


def minimumNumber(n: int, password: str) -> int:
    res = 0
    criterias = [False for _ in range(4)]

    for char in password:
        if char.isdigit():
            criterias[0] = True
        if char.isalpha() and char.islower():
            criterias[1] = True
        if char.isalpha() and char.isupper():
            criterias[2] = True
        if char in "!@#$%^&*()-+":
            criterias[3] = True

    return max(criterias.count(False), 6 - len(password))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + "\n")
    fptr.close()
