class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    """Add a node at the end"""
    def append(self, data):
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    """Print all elements in the list"""
    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
     
    """Delete the n-th node (1-based index)"""
    def delete_nth(self, n):
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list")
            if n <= 0:
                raise ValueError("Index must be a positive integer (1-based)")

            if n == 1:
                print(f"Deleting node at position {n}: {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            prev = None
            count = 1

            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if current is None:
                raise IndexError("Index out of range")

            print(f"Deleting node at position {n}: {current.data}")
            prev.next = current.next

        except Exception as e:
            print(f"Error: {e}")

# Test the Program
if __name__ == "__main__":
    ll = LinkedList()

    # Append elements to the list
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("REAL List:")
    ll.print_list()

    print("\nDeleting 2nd node:")
    ll.delete_nth(2)
    ll.print_list()

    print("\nDeleting 3rd node:")
    ll.delete_nth(3)
    ll.print_list()

    print("\nDeleting 6th node (out of range):")
    ll.delete_nth(6)

    print("\nDeleting remaining nodes:")
    ll.delete_nth(1)
    ll.delete_nth(1)
    ll.print_list()

    print("\nTrying to delete from an empty list:")
    ll.delete_nth(1)
