class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        hash_num = {}


        for i in range(len(numbers)):
            compliment = target - numbers[i]

            if compliment in hash_num:
                return [hash_num[compliment]+1 , i+1 ]
            
            hash_num[numbers[i]] = i
        return []
        