class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def Insert_At_Beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def Insert_At_End(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.data = None
        for data in data_list:
            self.Insert_At_End(data)

if __name__=='__main__':
    ll = LinkedList()
    # ll.Insert_At_Beginning(5)
    ll.insert_values(["apple","mango","banana"])
    # ll.Insert_At_End(15)
    # ll.Insert_At_End(20)
    # ll.Insert_At_End(25)
    ll.print()