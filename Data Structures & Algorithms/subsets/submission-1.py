class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets =[[]]

        for num in nums:
        # Create new subsets by adding the current number to all existing subsets
              new_subsets = [current_subset + [num] for    current_subset in subsets]
              subsets.extend(new_subsets)
        
        return subsets
        