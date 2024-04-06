import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        err = 0.00000000000001
        power = math.log(n, 3)
        power_int = int(power) + 1 if abs(int(power) - power) > 0.5 else int(power)
        return abs(power_int - power) < err

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n > 0) and (1162261467 % n == 0)


assert Solution().isPowerOfThree(27) == True
assert Solution().isPowerOfThree(1) == True
assert Solution().isPowerOfThree(0) == False
assert Solution().isPowerOfThree(-1) == False
assert Solution().isPowerOfThree(9) == True