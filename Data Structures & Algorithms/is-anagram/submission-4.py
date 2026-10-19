class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        
        i = 0
        if len(s) >= len(t):
            u = s
        else:
            u = t

        while i <= len(u) - 1:
            try:
                if s[i] != t[i]:
                    return False
            except IndexError:
                return False
            i += 1
        
        return True
        