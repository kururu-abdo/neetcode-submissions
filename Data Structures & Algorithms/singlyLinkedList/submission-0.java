class LinkedList {
    private class Node {
        int value;
        Node next;

        Node(int value) {
            this.value = value;
            this.next = null;
        }
    }

    private Node head;

    public LinkedList() {
        head = null;
    }

    public int get(int index) {
        Node current = head;

        for (int i = 0; i < index; i++) {
            if (current == null) {
                return -1;
            }
            current = current.next;
        }

        // This handles both an empty list and an index past the end.
        if (current == null) {
            return -1;
        }

        return current.value;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = head;
        head = newNode;
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);

        if (head == null) {
            head = newNode;
            return;
        }

        Node current = head;

        while (current.next != null) {
            current = current.next;
        }

        current.next = newNode;
    }

    public boolean remove(int index) {
        if (head == null) {
            return false;
        }

        if (index == 0) {
            head = head.next;
            return true;
        }

        Node current = head;

        // Move to the node immediately before the target.
        for (int i = 0; i < index - 1; i++) {
            if (current.next == null) {
                return false;
            }
            current = current.next;
        }

        // There is no node at the requested index.
        if (current.next == null) {
            return false;
        }

        // Skip over the node being removed.
        current.next = current.next.next;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>();
        Node current = head;

        while (current != null) {
            values.add(current.value);
            current = current.next;
        }

        return values;
    }
}