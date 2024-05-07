class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0

        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBegin(3)
    ll.insertAtBegin(2)
    ll.insertAtBegin(1)
    print("Linked List after insertion at beginning:")
    ll.printList()

    ll.insertAtIndex(4, 2)  
    print("Linked List after insertion at index 2:")
    ll.printList()

    ll.insertAtIndex(5, 10)  
