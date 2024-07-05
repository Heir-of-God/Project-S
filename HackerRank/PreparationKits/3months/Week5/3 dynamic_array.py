import os


def dynamicArray(n: int, queries: list[list[int]]) -> list[int]:
    arr = [[] for _ in range(n)]
    res = []
    last_answer = 0

    for q in queries:
        query_type = q[0]
        for_xor = q[1]
        value = q[2]

        if query_type == 1:
            arr[(for_xor ^ last_answer) % n].append(value)
        else:
            idx = (for_xor ^ last_answer) % n
            last_answer = arr[idx][value % len(arr[idx])]
            res.append(last_answer)

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
