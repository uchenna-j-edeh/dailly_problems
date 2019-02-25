# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = item
        temp.next = self.head
        self.head = temp        

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        firstList = LinkedList()
        for lt in l1:
            firstList.add(lt)

        secondList = LinkedList()
        for lt in l2:
            secondList.add(lt)            
        
        result = []

        firstCurr = firstList.head
        secondCurr = secondList.head
        remainder = 0
        mySum = 0

        while firstCurr != None:          
            if (firstCurr.val + secondCurr.val + remainder) / 10 > 0:
                mySum = (firstCurr.val + secondCurr.val + remainder) % 10
                remainder = (firstCurr.val + secondCurr.val + remainder) / 10
            else:
                mySum = firstCurr.val + secondCurr.val + remainder
                remainder = 0

            result.append(mySum)
            firstCurr = firstCurr.next
            secondCurr = secondCurr.next

        if remainder:
           result.append(remainder)
        return result


x1 = ListNode(2)
x2 = ListNode(4)
x3 = ListNode(3)

xlt = [x3, x2, x1 ]

y1 = ListNode(5)
y2 = ListNode(6)
y3 = ListNode(4)

ylt = [y3, y2, y1]

Sol = Solution()

print Sol.addTwoNumbers(xlt, ylt)

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = item
        temp.next = self.head
        self.head = temp        

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        firstList = LinkedList()
        for lt in l1:
            firstList.add(lt)

        secondList = LinkedList()
        for lt in l2:
            secondList.add(lt)            
        
        result = []

        firstCurr = firstList.head
        secondCurr = secondList.head
        remainder = 0
        mySum = 0

        while firstCurr != None:          
            if (firstCurr.val + secondCurr.val + remainder) / 10 > 0:
                mySum = (firstCurr.val + secondCurr.val + remainder) % 10
                remainder = (firstCurr.val + secondCurr.val + remainder) / 10
            else:
                mySum = firstCurr.val + secondCurr.val + remainder
                remainder = 0

            result.append(mySum)
            firstCurr = firstCurr.next
            secondCurr = secondCurr.next

        if remainder:
           result.append(remainder)
        return result


x1 = ListNode(2)
x2 = ListNode(4)
x3 = ListNode(3)

xlt = [x3, x2, x1 ]

y1 = ListNode(5)
y2 = ListNode(6)
y3 = ListNode(4)

ylt = [y3, y2, y1]

Sol = Solution()

print Sol.addTwoNumbers(xlt, ylt)


