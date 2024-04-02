def twoSum(nums, target):
    mem = {}
    for idx, num in enumerate(nums):
        if target-num in mem:
            return [mem[target-num], idx]
        mem[num] = idx
    return


assert twoSum([2,7,11,15], 9) == [0, 1]
assert twoSum([3,2,4], 6) == [1, 2] 
assert twoSum([3,3], 6) == [0, 1]