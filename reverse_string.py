from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        n = len(s)
        for i in range(mid):
            s[i], s[n-i-1] = s[n-i-1], s[i]


s = ["h","e","l","l","o"]
Solution().reverseString(s)
assert s == ["o","l","l","e","h"]

s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
assert s == ["h","a","n","n","a","H"]
        