from typing import List


def quick_sort(nums: List[int], low, high) -> None:
    """Given nums returns in ascending order

    Key points:
    - Each time select a num split:
        Divide into two from mid, and then sort left/right

    - Only stable and O(NLogN solution)
        - Space complexity O(N)
    """
    if low < high:
        pivot = partition(nums, low, high)

        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    """The target of partitions is, given an array and an element r of the array as a pivot,
    put r at its correct position in a sorted array and put all smaller elements (smaller than r) before r,
    and put all greater elements (greater than r) after r. All this should be done in linear time.

    Args:
        arr: call stack array
        low: pointer to the
    """
    pivot = arr[high]

    pointer = low

    for i in range(low, high):
        if arr[i] <= pivot:
            arr[pointer], arr[i] = arr[i], arr[pointer]
            pointer += 1

    arr[pointer], arr[high] = arr[high], arr[pointer]
    return pointer + 1

    # #extra space
    # smaller, larger = [], []
    # pivot = arr[high]
    # for i in range(low, high):
    #     if arr[i] <= pivot:
    #         smaller.append(arr[i])
    #     else:
    #         larger.append(arr[i])

    # # modify the arr
    # arr[low : high + 1] = smaller + [pivot] + larger
    # return low + len(smaller)


if __name__ == "__main__":
    import time
    import random

    # test = [1, 3, 100, 2, 9, 15, 4]
    # quick_sort(test, 0, len(test) - 1)
    # print(test)

    time_complexity_check = []
    for n in (10, 100, 1000):
        start = time.time()
        nums = [random.randint(0, 1000) for _ in range(n)]
        quick_sort(nums, 0, len(nums) - 1)
        duration = time.time() - start
        assert nums == sorted(nums)
        time_complexity_check.append(duration)

    print(f"Time complexity {time_complexity_check}")
