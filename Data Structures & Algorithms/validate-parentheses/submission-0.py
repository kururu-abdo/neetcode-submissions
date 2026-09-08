class Solution:
    def isValid(self, s: str) -> bool:
        traces = {")":"(" , "}":"{" , "]" :"["}
        stack = []

        for char in s:
            if char in traces:
                top_element = stack.pop() if stack else "#"
                if traces[char] != top_element:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
    
        