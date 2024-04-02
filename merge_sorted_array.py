from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        end = n + m - 1

        while left > -1 and right > - 1:

            if nums1[left] > nums2[right]:
                nums1[end] = nums1[left]
                left -= 1
            else:
                nums1[end] = nums2[right]
                right -= 1
            end -= 1
        
        while left > - 1:
            nums1[end] = nums1[left]
            left -= 1
            end -= 1
        while right > - 1:
            nums1[end] = nums2[right]
            right -= 1
            end -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
assert nums1 == [1,2,2,3,5,6]


nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
assert nums1 == [1]



nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
assert nums1 == [1]