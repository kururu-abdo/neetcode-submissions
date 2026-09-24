class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        // 1. Add all numbers to a HashSet for O(1) lookups
        val numSet = nums.toHashSet()
        var longestStreak = 0

        for (num in numSet) {
            // 2. Check if 'num' is the START of a sequence
            // If num - 1 exists, 'num' is not the start, so skip it!
            if (!numSet.contains(num - 1)) {
                var currentNum = num
                var currentStreak = 1

                // 3. Count how far this sequence goes
                while (numSet.contains(currentNum + 1)) {
                    currentNum += 1
                    currentStreak += 1
                }

                // 4. Update our global maximum
                longestStreak = maxOf(longestStreak, currentStreak)
            }
        }

        return longestStreak
    }
}
