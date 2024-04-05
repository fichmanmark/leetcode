class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = dict()
        for ch in s:
            h[ch] = h.get(ch, 0) + 1
        for ch in t:
            if ch not in h:
                return False
            if h[ch] == 0:
                return False
            h[ch] -= 1

        return sum(h.values()) == 0

s = "anagram"
t = "nagaram"
assert Solution().isAnagram(s, t) 


s = "rat"
t = "car"
assert not Solution().isAnagram(s, t)


s = "aacc"
t = "ccac"
assert not Solution().isAnagram(s, t)