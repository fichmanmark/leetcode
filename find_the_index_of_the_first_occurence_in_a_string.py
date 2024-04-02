class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

class Solution:

    def lps(self, pat):
        l = 0
        lps = [0] * len(pat)
        i = 1
        while i < len(pat):
            if pat[i] == pat[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
                
    def KMP(self, txt: str, pat: str) -> int:
        lps = self.lps(pat)
        M = len(pat)
        N = len(txt)
        
        i, j = 0, 0
        while (N - i) >= (M - j):
            if pat[j] == txt[i]:
                i += 1  
                j += 1
            if j == M:
                return i - j
            elif (i < N) and (pat[j] != txt[i]):
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        return self.KMP(txt=haystack, pat=needle)



haystack = "sadbutsad"
needle = "sad"
assert Solution().strStr(haystack=haystack, needle=needle) == 0 


haystack = "leetcode"
needle = "leeto"
assert Solution().strStr(haystack=haystack, needle=needle) == -1