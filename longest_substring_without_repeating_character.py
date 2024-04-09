# MEDIUM

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        mem = {}
        left, res = 0, 0
        for right in range(len(s)):
            print(left, right, res, mem)
            if s[right] not  in mem or mem[s[right]] < left:
                mem[s[right]] = right
                res = max(res, right-left + 1)
            else:
                left = mem[s[right]] + 1
                mem[s[right]] = right

        return max(res, right - left)
        
            

assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
