class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum(((ord(ch) - 64) * 26 ** idx for idx, ch in enumerate(columnTitle[::-1])))

assert Solution().titleToNumber("A") == 1
assert Solution().titleToNumber("AB") == 28
assert Solution().titleToNumber("ZY") == 701
assert Solution().titleToNumber("ZZ") == 702
assert Solution().titleToNumber("AAA") == 703
