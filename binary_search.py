from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while right - left > 1:
            m = (left + right) // 2
            if target < nums[m]:
                right = m
            else:
                left = m
        print(left)
        return left if target == nums[left] else -1




nums = [-1,0,3,5,9,12]
target = 9
assert Solution().search(nums, target) == 4

nums = [-1,0,3,5,9,12]
target = 2
assert Solution().search(nums, target) == -1


nums = [2, 5]
target = 5
assert Solution().search(nums, target) == 1