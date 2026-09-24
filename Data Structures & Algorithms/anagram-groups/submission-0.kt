class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        // Map to group words by their sorted character key
        val anagramMap = HashMap<String, MutableList<String>>()

        for (item in strs) {
            // 1. Sort the characters of the current string to create a key
            // e.g., "tea" -> ['t', 'e', 'a'] -> ['a', 'e', 't'] -> "aet"
            val sortedKey = item.toCharArray().sorted().joinToString("")

            // 2. If the key doesn't exist, initialize a new mutable list
            if (!anagramMap.containsKey(sortedKey)) {
                anagramMap[sortedKey] = mutableListOf()
            }

            // 3. Add the original word to its corresponding anagram group
            anagramMap[sortedKey]?.add(item)
        }

        // 4. Return all grouped values as a List<List<String>>
        return anagramMap.values.toList()
    }
}
