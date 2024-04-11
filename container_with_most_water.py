# MEDIUM

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        m = 0
        while left < right:
            m_current = (right - left) * min(height[left], height[right])
            m = m if m > m_current else m_current
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m

assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxArea([1, 1]) == 1
assert Solution().maxArea([1,2,4,3]) == 4
assert Solution().maxArea([1,0,0,0,0,0,0,2,2]) == 8
assert Solution().maxArea([2,3,10,5,7,8,9]) == 36
assert Solution().maxArea([2,3,4,5,18,17,6]) == 17
assert Solution().maxArea([1,3,2,5,25,24,5]) == 24
assert Solution().maxArea([1,2,3,4,5,25,24,3,4]) == 24
assert Solution().maxArea([6,4,3,1,4,6,99,62,1,2,6]) == 62
assert Solution().maxArea([1,8,100,2,100,4,8,3,7]) == 200
assert Solution().maxArea([4,6,4,4,6,2,6,7,11,2]) == 42





