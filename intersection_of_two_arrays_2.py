from typing import List

from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        d = defaultdict(int)
        if n1 > n2:
            for i in nums2:
                d[i] += 1
        else:
            for i in nums1:
                d[i] += 1
        res = []
        if n1 > n2:
            for i in nums1:
                if i in d:
                    if d[i] > 0:
                        res.append(i)
                        d[i] -= 1
        else:
            for i in nums2:
                if i in d:
                    if d[i] > 0:
                        res.append(i)
                        d[i] -= 1
        return res
        

assert Solution().intersect([1,2,2,1], [2,2]) == [2,2]
assert Solution().intersect([4,9,5], [9,4,9,8,4]) in  [[4,9], [9, 4]]