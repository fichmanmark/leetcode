from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0
        cnt = 0
        n = len(nums)
        if n == 1:
            return nums
        for i in range(n):
            if nums[i] != 0:
                nums[start] = nums[i]
                if start != i:
                    nums[i] = 0
                start += 1
            else:
                cnt += 1
            
            if n - i == cnt and cnt > 0:
                nums[i] = 0
                cnt -= 1
        return nums
    

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums



assert Solution().moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
assert Solution().moveZeroes([0]) == [0]
assert Solution().moveZeroes([0,1,0]) == [1,0,0]