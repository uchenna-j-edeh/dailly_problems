class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def insertAtHead(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head.next_element
        self.head.next_element = temp_node
        return self.head


    def isEmpty(self):
        if self.head.next_element == None:
            return True
        else:
            return False

    def insertAtTail(self, data):
        if self.head.next_element is None:
            self.head.next_element = Node(data)
            return self.head

        temp = self.head.next_element
        while(temp.next_element != None):
            temp = temp.next_element

        temp.next_element = Node(data)
        return temp

    def search(self, value):
        if self.head.next_element == None:    
            return False
  
        temp = self.head.next_element
        while(temp != None):
            if temp.data == value:
                return True

            temp = temp.next_element    

        return False

            

    def printList(self):
        if(self.isEmpty()):
            print("List is empty")
            return False

        temp = self.head.next_element
        while(temp.next_element != None):
            print temp.data, "->", 
            temp = temp.next_element

        print temp.data, "-> None"
        return True
 
hlist = LinkedList()
hlist.printList()

for i in range(1, 100):
    hlist.insertAtHead(i)

hlist.printList()
print(hlist.search(100))

tlist = LinkedList()
tlist.printList()

for i in range(1, 100):
    tlist.insertAtTail(i)

tlist.printList()
print(tlist.search(99))
print(tlist.search(1))

