import sys


def camel_apply(inp: str) -> None:
    inp: str = inp.strip()
    operation: str = inp[0]
    object_type: str = inp[2]
    string: str = inp[4:]

    if operation == "S":
        string = string[0].lower() + string[1:] + "("
        res: str = ""
        cur_ind = 0
        while string[cur_ind] != "(":
            if string[cur_ind].isupper():
                res += " "
            res += string[cur_ind].lower()
            cur_ind += 1
    elif operation == "C":
        res = "".join([word.capitalize() for word in string.split()])
        if object_type != "C":
            res = res[0].lower() + res[1:]
        if object_type == "M":
            res += "()"

    print(res)


for line in sys.stdin:
    camel_apply(line)
