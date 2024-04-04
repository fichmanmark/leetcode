class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += n & 1
            n = n >> 1
        return res

assert Solution().hammingWeight(11) == 3
assert Solution().hammingWeight(128) == 1
assert Solution().hammingWeight(2147483645) == 30