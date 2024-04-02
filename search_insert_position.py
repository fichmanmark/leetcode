from typing import List

def searchInsert(nums:List[int], target:int) -> int:
    left, right = 0, len(nums)

    while right - left > 1:
        m = (right + left) // 2
        if nums[m] > target:
            right = m
        else:
            left = m


    if nums[left] == target:
        return left
    elif nums[left] > target:
        return left
    else:
        return left + 1
    


nums = [1,3,5,6]
target = 5
assert searchInsert(nums, target) == 2

nums = [1,3,5,6]
target = 2
assert searchInsert(nums, target) == 1


nums = [1,3,5,6]
target = 7
assert searchInsert(nums, target) == 4