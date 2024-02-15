from typing import List


def bubble_sort(nums: List[int]) -> None:
    """Given nums returns in ascending order

    Key points:
    - Each time a num is compared with the adjacent and exchange until reach the end
        - Maximum one will be bubbled to the end
    - Modify inplace
    - The time complexity on average is O(N^2)
    """
    for i in range(len(nums) - 1):
        swap = 0
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap += 1
        if swap == 0:
            break


if __name__ == "__main__":
    import time
    import random

    time_complexity_check = []
    for n in (10, 100, 1000):
        start = time.time()
        nums = [random.randint(0, 1000) for i in range(n)]
        bubble_sort(nums)
        duration = time.time() - start
        time_complexity_check.append(duration)
        print(nums)

    print(f"Time complexity {time_complexity_check}")
