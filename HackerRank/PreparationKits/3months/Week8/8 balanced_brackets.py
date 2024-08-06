import os


def isBalanced(s: str) -> str:
    matching: dict[str, str] = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack.pop() != matching[char]:
                return "NO"

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + "\n")
    fptr.close()
