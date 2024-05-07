class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtEnd(1)
    ll.insertAtEnd(2)
    ll.insertAtEnd(3)
    print("Linked List after insertion at end:")
    ll.printList()
