class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        s1_counts = [0] * 26
        window_counts = [0] * 26


        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
        # Slide the window from index len(s1) to the end of s2
        for i in range(len(s1), len(s2)):
               if s1_counts == window_counts:
                    return True
                 # Add the incoming character (Right side)
               right_char = s2[i]
               window_counts[ord(right_char) - ord('a')] += 1
    
    # Remove the outgoing character (Left side)
               left_char = s2[i - len(s1)]
               window_counts[ord(left_char) - ord('a')] -= 1

        
   

        return s1_counts ==window_counts
