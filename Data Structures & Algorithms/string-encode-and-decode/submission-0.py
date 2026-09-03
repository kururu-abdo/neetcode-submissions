class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = []
        for s in strs:
            encoded_result.append(f"{len(s)}#{s}")
        return "".join(encoded_result)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                 j += 1
            length = int(s[i:j])
            start_of_str = j + 1
            end_of_str = start_of_str + length
            decoded_strs.append(s[start_of_str:end_of_str])
            i = end_of_str
        return  decoded_strs     
                 
                      
