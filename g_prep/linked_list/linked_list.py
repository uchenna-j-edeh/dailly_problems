class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_to_tail(self, d):
        node = Node(d)
        current = self.head
        if self.head:
            while current.next:
                current = current.next

            current.next = node
        else:
            self.head = node

    def print_nodes(self):
        current = self.head
        if self.head:
            while current.next:
                print(current.data)
                current = current.next
            print(current.data) # last node

        return None

    def delete_node(self, d):
        if not self.head:
            return
        if self.head.data == d: # remember self.head is a reference to the first node. 
            self.head = self.head.next # self.head.next is the node following the first node, self.head.data is the data of the first node
            return self.head

        current = self.head
        while current.next:
            if current.next.data == d:
                current.next = current.next.next
                return self.head
            current = current.next
        return self.head

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):
        ll.add_to_tail(i)

    print('-'*10)
    ll.delete_node(7) # test middle element removal
    ll.print_nodes()
    print('-'*10)
    ll.delete_node(0) # test head element removal
    ll.print_nodes()
    print('-'*10)
    ll.delete_node(9) # test last element removal
    ll.print_nodes()
    print('-'*10)
    ll.print_nodes()

