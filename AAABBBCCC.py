def f(s):
    res = s[0]
    cur = s[0]
    for i in range(1, len(s)):
        if cur == s[i]:
            pass
        else:
            cur = s[i]
            res += s[i]
    return res



print(f("AAAAABBBBCCCCDDF"))