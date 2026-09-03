from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        if len(s) != len(t):
            return False
        
        t=t.lower()
        s=s.lower()

        return Counter(s) == Counter(t)