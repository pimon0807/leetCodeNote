class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        for i in range(0,len(s)):
            if self.xor(s[i] not in hashMapS, t[i] not in hashMapT):
                return False
            elif s[i] not in hashMapS and t[i] not in hashMapT:
                hashMapS[s[i]] = t[i]
                hashMapT[t[i]] = s[i]
                s = s[:i] + t[i] + s[i+1:]
            else:
                s = s[:i] + hashMapS[s[i]] + s[i+1:]

        return True if s == t else False
    
    def xor(self, a, b):
        return bool(a) != bool(b)