from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mem = Counter(s)
        for i in range(len(s)):
            if mem[s[i]] == 1:
                return i
        return -1


assert Solution().firstUniqChar('leetcode') == 0
assert Solution().firstUniqChar('loveleetcode') == 2
assert Solution().firstUniqChar('aabb') == -1