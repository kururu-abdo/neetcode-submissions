class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        upper = len(nums)-1
        lower = 0
       
        while lower <= upper:
            mid = lower+ (upper-lower) // 2
            if nums[mid]== target:
               return mid
            elif nums[mid] < target:
                lower = mid+1
            else: 
                upper = mid-1    
        return -1

