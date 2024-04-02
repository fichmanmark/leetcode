class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = [ch for ch in s.lower() if (ord('a') <= ord(ch) <= ord('z')) or (ord('0') <= ord(ch) <= ord('9'))]
        return clean_str == clean_str[::-1]
    

assert Solution().isPalindrome("A man, a plan, a canal: Panama")
assert not Solution().isPalindrome("race a car")
assert Solution().isPalindrome(" ")

assert not Solution().isPalindrome("0P")


