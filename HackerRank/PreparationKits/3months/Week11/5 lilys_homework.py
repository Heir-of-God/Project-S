import os


def count_swaps_from_a_to_b(a: list[int], b: list[int]) -> int:
    n: int = len(a)
    value_to_index: dict[int, int] = {val: ind for ind, val in enumerate(a)}
    index_to_value: dict[int, int] = {ind: val for ind, val in enumerate(a)}
    res = 0

    for cur_ind in range(n):
        right_element_here: int = b[cur_ind]
        if value_to_index[right_element_here] != cur_ind:
            res += 1
            index_to_swap: int = value_to_index[right_element_here]
            value_here: int = index_to_value[cur_ind]
            # swap index_to_swap and cur_ind + value_here and right_element_here
            value_to_index[value_here], value_to_index[right_element_here] = index_to_swap, cur_ind
            index_to_value[cur_ind], index_to_value[index_to_swap] = right_element_here, value_here

    return res


def lilysHomework(arr: list[int]) -> int:
    srt1: list[int] = sorted(arr)
    srt2: list[int] = sorted(arr, reverse=True)
    return min(count_swaps_from_a_to_b(arr, srt1), count_swaps_from_a_to_b(arr, srt2))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = lilysHomework(arr)
    fptr.write(str(result) + "\n")
    fptr.close()
