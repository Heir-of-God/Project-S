import os


def weightedUniformStrings(s: str, queries: list[int]) -> list[str]:
    weights = set()
    left = 0
    prev = "_"

    for ind, char in enumerate(s):
        if char != prev:
            left = ind
        weight = (ind - left + 1) * (ord(char) - ord("a") + 1)
        if weight not in weights:
            weights.add(weight)
        prev = char

    return ["Yes" if q in weights else "No" for q in queries]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    fptr.write("\n".join(result))
    fptr.write("\n")
    fptr.close()
