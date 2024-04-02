def romanToInt(s: str) -> int:
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    res = m[s[-1]]
    prev = s[-1]
    for l in s[-2::-1]:
        if m[l] < m[prev]:
            res -= m[l]
        else:
            res += m[l]
        prev = l

    return res


assert romanToInt('III') == 3
assert romanToInt('LVIII') == 58
assert romanToInt('MCMXCIV') == 1994
