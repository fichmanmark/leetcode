# MEDIUM

class Solution:

    def expand_from_center(self, s, start_left, start_right):
        found = 0
        while start_left >= 0 and start_right < len(s):
            if s[start_left] == s[start_right]:
                start_left -= 1
                start_right += 1
                found = 1
            else:
                break
        return s[start_left+1:start_right] if found else ''

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if s[::-1] == s:
            return s
        
        longest = s[0]
        for i in range(len(s)):
            even = self.expand_from_center(s, i, i+1)
            odd = self.expand_from_center(s, i-1, i+1)
            if len(even) > len(longest):
                longest = even
            if len(odd) > len(longest):
                longest = odd
        print(longest)
        return longest



assert Solution().longestPalindrome("aaaa") == "aaaa"
assert Solution().longestPalindrome("babad") == "bab"
assert Solution().longestPalindrome("cbbd") == "bb"
assert Solution().longestPalindrome("aaaacaaaa") == "aaaacaaaa"
assert Solution().longestPalindrome("aaaaplpaat") == "aaplpaa"
assert Solution().longestPalindrome("ccd") == "cc"


