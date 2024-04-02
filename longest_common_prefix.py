def longestCommonPrefix(strs) -> str:
    prefix = strs[0]
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if len(s) == len(prefix[:i]):
                return prefix[:i]
            if s[i] != prefix[i]:
                return prefix[:i]
                    
    return prefix



assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert longestCommonPrefix(["dog","racecar","car"]) == ""
assert longestCommonPrefix(["ab", "a"]) == "a"

