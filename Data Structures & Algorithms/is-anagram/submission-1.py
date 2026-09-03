from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        if len(s) != len(t):
            return False
        
        t=t.lower()
        s=s.lower()

        char_counts ={}

        for char in t:
          if char  not in char_counts:
             char_counts[char]= 1
          else:
             char_counts[char]+=1
        for char in s:
           if char in char_counts:
              char_counts[char]-=1
           else:
            return False

       
        for count in char_counts.values():
           if count!=0:
             return False

        return True 
              


    