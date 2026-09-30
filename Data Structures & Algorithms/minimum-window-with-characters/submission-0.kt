class Solution {
    fun minWindow(s: String, t: String): String {
        if (s.isEmpty() || t.isEmpty() || s.length < t.length) return ""

        // 1. Map to store the frequency of characters required from string 't'
        val tFreq = IntArray(128)
        for (char in t) {
            tFreq[char.code]++
        }

        // 2. Sliding window pointers and tracking variables
        var left = 0
        var right = 0
        var requiredCount = t.length
        
        // Tracking details for the optimal window found
        var minLength = Int.MAX_VALUE
        var minLeftStart = 0

        // 3. Expand the right boundary of the window
        while (right < s.length) {
            val rightChar = s[right]
            
            // If this character is needed by 't', decrement our required match counter
            if (tFreq[rightChar.code] > 0) {
                requiredCount--
            }
            // Decrement the frequency inside our active window tracker
            tFreq[rightChar.code]--
            right++

            // 4. Shrink the window from the left once all characters are matched
            while (requiredCount == 0) {
                // Update the global minimum substring bounds if a shorter window is found
                val currentWindowLength = right - left
                if (currentWindowLength < minLength) {
                    minLength = currentWindowLength
                    minLeftStart = left
                }

                val leftChar = s[left]
                // Put the leftmost character back out of the window
                tFreq[leftChar.code]++
                
                // If this character was a critical requirement for 't', we no longer have a valid window
                if (tFreq[leftChar.code] > 0) {
                    requiredCount++
                }
                left++
            }
        }

        // 5. Return the substring if a valid window was found, otherwise return empty string
        return if (minLength == Int.MAX_VALUE) "" else s.substring(minLeftStart, minLeftStart + minLength)
    }
}
