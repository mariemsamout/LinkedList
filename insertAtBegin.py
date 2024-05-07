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
    print("Linked List after insertion:")
    ll.printList()
