from typing import List


def merge_sort(nums: List[int]) -> None:
    """Given nums returns in ascending order

    Key points:
    - Each time select a num split:
        Divide into two, usually use the mid

    - Only stable and O(NLogN solution)
        - Space complexity O(N)
    """
    if len(nums) > 1:
        mid = len(nums) // 2
        # Recursive call
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        # Now the left and right may not be the same length
        # But we can assume they are sorted
        i, j, k = 0, 0, 0
        """
        i, j serves as the iterators for left, right array
        k is the pointer change nums inplace,
            here the nums is the new one in call stack
        """
        while i < len(left) and j < len(right):
            # compare and insert into nums
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
            # Now it could be one of left and right array reach the end

        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1


if __name__ == "__main__":
    import time
    import random

    time_complexity_check = []
    for n in (10, 100, 1000):
        start = time.time()
        nums = [random.randint(0, 1000) for _ in range(n)]
        merge_sort(nums)
        duration = time.time() - start
        time_complexity_check.append(duration)
        print(nums)

    print(f"Time complexity {time_complexity_check}")
