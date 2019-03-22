
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_position(self, position):
        current = self.head
        count = 0
        if self.head:
            while current.next:
                count = count + 1
                if (count == position):
                    return current
                current = current.next # here is when i actually advance to the next node
            count = count + 1 # last node
            if count == position:
                return current

        return None

    def insert(self, new_element, position):
        current = self.head
        count = 0
        if self.head:
            while current.next:
                count = count + 1
                if (count == position):
                    new_element.next = current.next
                    current.next = new_element
                    break
                current = current.next # here is when i actually advance to the next node
        else:
            self.head = new_element
 
    def insert_v2(self, new_element, position):
        element = self.get_position(position)
        if element:
            new_element.next = element.next
            element.next = new_element
        

    def print_nodes(self):
        current = self.head
        if self.head:
            while current.next:
                print(current.value)
                current = current.next
            print(current.value) #last node

        return None

if __name__ == "__main__":
    llist = LinkedList()
#    node = Node('Uchenna')
#    llist.append(node)
    for i in range(10):
        node = Node(i)
        llist.append(node)

    llist.print_nodes()
    print(llist.get_position(5))
    print(llist.get_position(25))
    print(llist.get_position(1))

    nodex = Node(45) 
    nodey = Node(55) 
    llist.insert(nodex, 5)
    llist.append(nodey)
    llist.print_nodes()
