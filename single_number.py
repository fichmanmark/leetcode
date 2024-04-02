def singleNumber(nums):
    res = 0
    for i in nums:
        res ^= i
    return res

from functools import reduce

def singleNumber(nums):
    return reduce(lambda x, y: x^y, nums)

nums = [2, 2, 1]
assert singleNumber(nums) == 1


nums = [4,1,2,1,2]
assert singleNumber(nums) == 4


nums = [1]
assert singleNumber(nums) == 1