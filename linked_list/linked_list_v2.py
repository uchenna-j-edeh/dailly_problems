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

    def insert(self, value, insertion_point):
        if self.head.next_element is None:
            self.head.next_element = Node(value)

        temp = self.head.next_element
        while(temp.next_element != None):
            if temp.data == insertion_point:
                new_node = Node(value)
                new_node.next_element = temp.next_element
                temp.next_element = new_node
                return True

            temp = temp.next_element
        
        return False
    
    def delete(self, value):
        if self.head.next_element == None:
            return False

        previous = None
        temp = self.head.next_element
        if temp.data == value: # when we only have one element to delete
            self.deleteAtHead()

        while(temp.next_element != None):
            if temp.data == value:
                previous.next_element = temp.next_element
                return True

            previous = temp
            temp = temp.next_element

        if temp.data == value:
            previous.next_element = temp.next_element
            return True

        return False

    def deleteAtHead(self):
        if self.head.next_element is None:
            return False

        self.head.next_element = self.head.next_element.next_element
        return True   

    def append(self, value):
        self.insertAtTail(value)
        
        

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
count = 10
for i in range(1, count):
    hlist.insertAtHead(i)

hlist.printList()
print(hlist.search(count))
hlist.insert(90000, 8)
hlist.printList()
hlist.delete(90000)
hlist.printList()
hlist.append(0)
hlist.printList()
hlist.deleteAtHead()
hlist.printList()


# tlist = LinkedList()
# tlist.printList()

# for i in range(1, count):
#     tlist.insertAtTail(i)

# tlist.printList()
# print(tlist.search(99))
# print(tlist.search(1))

