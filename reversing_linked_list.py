# let's reverse a linked list in Python...
# more comments coming soon... (hopefully)

# Define the Node class to represent a single node in the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class and create a simple linked list, also add a reverse method.
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

    def reverse(self):
        prev = None
        current = self.head
        # A good way to understand the below is to visualise
        # the pointer arrows in your head, and take it one step
        # at a time.
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

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
linked_list.reverse()
linked_list.display()

# Create a new linked list and display it.
new_linked_list = LinkedList()
new_linked_list.append(5)
new_linked_list.append(6)
new_linked_list.append(7)
new_linked_list.append(8)
print("Original linked list:")
new_linked_list.display()

# Reverse the new linked list and display the reversed list.
new_linked_list.reverse()
print("Reversed linked list:")
new_linked_list.display()

