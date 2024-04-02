def isValid(s):
    d = {}
    stack = []
    d['('] = ')'
    d['{'] = '}'
    d['['] = ']'
    for ch in s:
        if ch in d:
            stack.append(ch)
        else:
            if len(stack) > 0:
                opened = stack.pop()
                if d[opened] != ch:
                    return False
            else:
                return False
    return len(stack) == 0


s = "()"
assert isValid(s) == True

s = "()[]{}"
assert isValid(s) == True

s = "(]"
assert isValid(s) == False

s = "([])"
assert isValid(s) == True

s = "["
assert isValid(s) == False

s = "]"
assert isValid(s) == False

