class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        
        while right - left > 1:
            m = (left + right) // 2
            if x < m * m:
                right = m
            else:
                left = m
        return left 
    

assert Solution().mySqrt(4) == 2
assert Solution().mySqrt(8) == 2

assert Solution().mySqrt(9) == 3