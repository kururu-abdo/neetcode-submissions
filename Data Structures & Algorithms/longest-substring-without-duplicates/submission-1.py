class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0;

        max_length=0
        left=0
        best=0

        hash = {}
        
        for right in range(len(s)):
            item= s[right]

            if item in hash and hash[item] >= left :
                left = hash[item]+1
            hash[item]= right

            max_length = max((right-left + 1) ,max_length )
        return max_length



        