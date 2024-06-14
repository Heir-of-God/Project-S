import os


def matchingStrings(strings, queries) -> list[int]:
    n: int = len(queries)
    q: set[int] = set(queries)
    count: dict[str, int] = {}
    for s in strings:
        if s in q:
            count[s] = count.get(s, 0) + 1

    for ind in range(n):
        queries[ind] = count.get(queries[ind], 0)
    return queries


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    strings_count = int(input().strip())
    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    queries_count = int(input().strip())
    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")
    fptr.close()
