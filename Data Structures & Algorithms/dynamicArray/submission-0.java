class DynamicArray {
 private int[] arr;
    private int size;
        public DynamicArray(int capacity) {
arr = new int[capacity];
        size = 0;
    }

    public int get(int i) {
 return arr[i];
    }

    public void set(int i, int n) {
 arr[i] = n;
    }

    public void pushback(int n) {
// Resize before inserting if there is no free space.
        if (size == arr.length) {
            resize();
        }

        arr[size] = n;
        size++;
    }

    public int popback() {
 size--;
        return arr[size];
    }

    private void resize() {
 int[] newArr = new int[arr.length * 2];

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        arr = newArr;
    }

    public int getSize() {
return size;
    }

    public int getCapacity() {
return arr.length;
    }
}
