# let's reverse a linked list in Python...

# Define the Node class to represent a single node in the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class and create a simple linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list and display it.
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.display()
