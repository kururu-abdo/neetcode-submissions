// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }

public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> result = new ArrayList<>();

        // There are no states for an empty input.
        if (pairs.isEmpty()) {
            return result;
        }

        // State before the first insertion.
        result.add(new ArrayList<>(pairs));

        for (int i = 1; i < pairs.size(); i++) {
            Pair current = pairs.get(i);
            int j = i - 1;

            // Shift larger elements to the right.
            // The strict '>' comparison keeps the sort stable.
            while (j >= 0 && pairs.get(j).key > current.key) {
                pairs.set(j + 1, pairs.get(j));
                j--;
            }

            // Insert current into its sorted position.
            pairs.set(j + 1, current);

            // Save a snapshot of the current array.
            result.add(new ArrayList<>(pairs));
        }

        return result;
    }
}