from random import randint


def partition(array: list[int], low: int, high: int) -> int:
    # this is function for choosing pivot and partitate the array
    pivot: int = array[randint(low, high)]
    write_ind_smaller: int = low  # where to write elements smaller than pivot
    write_ind_greater: int = high  # where to write elements greater than pivot
    cur = low

    while cur < write_ind_greater + 1:
        num = array[cur]
        if num < pivot:
            array[write_ind_smaller], array[cur] = array[cur], array[write_ind_smaller]
            write_ind_smaller += 1
        elif num > pivot:
            array[write_ind_greater], array[cur] = array[cur], array[write_ind_greater]
            write_ind_greater -= 1
        else:
            cur += 1

    return write_ind_smaller  # return index of the pivot


def quick_sort(array, low, high) -> None:  # [low, high) - inclusively
    # Base case: if range is empty or contains only 1 element
    if low >= high:
        return

    pivot_ind: int = partition(array, low, high)
    quick_sort(array, low, pivot_ind - 1)  # left part
    quick_sort(array, pivot_ind + 1, high)  # right part


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        quick_sort(nums, 0, len(nums))
        return nums


def merge_sort(array: list[int]) -> None:
    n: int = len(array)
    if n <= 1:
        return
    midle_ind: int = n // 2
    left_part: list[int] = array[:midle_ind][:]
    right_part: list[int] = array[midle_ind:][:]

    merge_sort(left_part)
    merge_sort(right_part)
    merge(left_part, right_part, array)


def merge(array1: list[int], array2: list[int], source_array: list[int]) -> None:
    p1: int = 0
    p2: int = 0
    n1: int = len(array1)
    n2: int = len(array2)
    write_ind = 0

    while p1 < n1 or p2 < n2:
        if p1 == n1 or (p2 != n2 and array2[p2] < array1[p1]):
            source_array[write_ind] = array2[p2]
            p2 += 1
        elif p2 == n2 or array1[p1] <= array2[p2]:
            source_array[write_ind] = array1[p1]
            p1 += 1
        write_ind += 1


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        counting: list[int] = [0 for _ in range(2 * 5 * 10**4 + 1)]
        for num in nums:
            # we add 5 * 10^4 because for smallest possible element -5 * 10^4 index must be 0
            counting[num + 5 * 10**4] += 1
        write_ind: int = 0
        for number_ind, freq in enumerate(counting):
            while freq != 0:
                nums[write_ind] = number_ind - 5 * 10**4
                write_ind += 1
                freq -= 1

        return nums
