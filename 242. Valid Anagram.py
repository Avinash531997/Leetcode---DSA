class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmapS, hmapT = {}, {}

        # Count occurrences in s
        for i in range(len(s)):
            hmapS[s[i]] = 1 + hmapS.get(s[i], 0)

        # Count occurrences in t
        for i in range(len(t)):
            hmapT[t[i]] = 1 + hmapT.get(t[i], 0)

        if hmapS==hmapT:
            return True
        return False
