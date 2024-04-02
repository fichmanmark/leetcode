from typing import List
from collections import Counter
def majorityElement(nums: List[int]) -> int:
    c = Counter(nums)
    return c.most_common()[0][0]

def majorityElement(nums: List[int]) -> int:
    c = -1
    votes = 0
    for i in range(len(nums)):
        if votes == 0:
            c = nums[i]
            votes += 1
        else:
            if c == nums[i]:
                votes += 1
            else:
                votes -= 1
    return c

assert majorityElement([3,2,3]) == 3
assert majorityElement([2,2,1,1,1,2,2]) == 2
