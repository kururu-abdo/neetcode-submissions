class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        result = []
        # This array will act as our window queue, storing indices
        window_indices = []

        for right in range(len(nums)):
            # 1. Slide window forward: Remove indices that fell out of bounds from the left
            if window_indices and window_indices[0] < right - k + 1:
                window_indices.pop(0)

            # 2. Maintain order: Remove elements smaller than the current element from the right
            while window_indices and nums[window_indices[-1]] < nums[right]:
                window_indices.pop()

            # 3. Add current element index
            window_indices.append(right)

            # 4. Once we have a valid window size of k, record the maximum
            if right >= k - 1:
                # The index of the maximum element is always at the front [0]
                result.append(nums[window_indices[0]])

        return result
            
