import os


def superReducedString(s: str) -> str:
    stack: list[str] = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack) if stack else "Empty String"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = superReducedString(s)
    fptr.write(result + "\n")
    fptr.close()
