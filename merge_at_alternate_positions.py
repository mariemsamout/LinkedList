class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def merge_at_alternate_positions(self, other_list):
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next

            current1.next = current2
            current2.next = next1

            current1 = next1
            current2 = next2

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    list2.append(8)

    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()

    list1.merge_at_alternate_positions(list2)
    print("Merged List:")
    list1.display()
