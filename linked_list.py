# class Node:
#     def __init__(self, data):
#         self.value = data
#         self.next = None

# Head = Tail = Node(10)

# Tail.next = Node(20)
# Tail = Tail.next

# Tail.next = Node(30)
# Tail = Tail.next

# class Li:
#     def __init__(self):
#         self.head = None

#     def printlist(self):
#         if self.head is None:
#             print("List is empty")
#         else:
#             temp = self.head
#             while temp:
#                 self.head = temp.next
                 

# print(Head.value, Head.next.value)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, position, data):
        if position < 0:
            raise ValueError("Position must be non-negative")
        if position == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next
        if not current:
            raise IndexError("Position out of range")
        new_node.next = current.next
        current.next = new_node

    def delete_at_start(self):
        if not self.head:
            raise IndexError("List is empty")
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            raise IndexError("List is empty")
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position < 0:
            raise ValueError("Position must be non-negative")
        if not self.head:
            raise IndexError("List is empty")
        if position == 0:
            self.delete_at_start()
            return
        current = self.head
        for _ in range(position - 1):
            if not current.next:
                raise IndexError("Position out of range")
            current = current.next
        current.next = current.next.next if current.next else None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def create_and_operate_linked_list():
    linked_list = LinkedList()
    num_nodes = int(input("Enter the number of nodes to create: "))

    for i in range(num_nodes):
        data = int(input(f"Enter data for node {i + 1}: "))
        linked_list.insert_at_end(data)

    print("Linked List after creation:")
    linked_list.print_list()

    while True:
        print("Choose an operation:")
        print("1. Insert at start")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete at start")
        print("5. Delete at end")
        print("6. Delete at position")
        print("7. Print list")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 8:
            break

        if choice == 1:
            data = int(input("Enter data to insert at the start: "))
            linked_list.insert_at_start(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            linked_list.insert_at_end(data)
        elif choice == 3:
            position = int(input("Enter position to insert: "))
            data = int(input("Enter data to insert at the position: "))
            linked_list.insert_at_position(position, data)
        elif choice == 4:
            linked_list.delete_at_start()
        elif choice == 5:
            linked_list.delete_at_end()
        elif choice == 6:
            position = int(input("Enter position to delete: "))
            linked_list.delete_at_position(position)
        elif choice == 7:
            linked_list.print_list()
        else:
            print("Invalid choice. Please try again.")

        print("Linked List after operation:")
        linked_list.print_list()

# Example usage:
create_and_operate_linked_list()
