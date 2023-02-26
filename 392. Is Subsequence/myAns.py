class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        matched = 0
        for i in t:
            if s[matched] == i:
                matched += 1
            if matched == len(s):
                return True
        return False