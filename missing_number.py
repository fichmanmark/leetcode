from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n+1) / 2 - sum(nums))


assert Solution().missingNumber([3,0,1]) == 2
assert Solution().missingNumber([0,1]) == 2
assert Solution().missingNumber([1,2]) == 0
assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8