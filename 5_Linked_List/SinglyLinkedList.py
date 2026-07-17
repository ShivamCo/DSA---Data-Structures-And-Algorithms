class Node:

    def __init__(self, info, next=None):

        self.info = info
        self.next = next 


class singlyLinkedList:

    def __init__(self, head=None):
        self.head = head 
    
    def insertAtEnd(self, info):
        temp = Node(info)

        if self.head is None:
            self.head = temp
            return

        t1 = self.head

        while t1.next is not None:
            t1 = t1.next
        
        t1.next = temp


    def insertAtBegn(self, info):
        temp = Node(info)

        temp.next = self.head
        self.head = temp

    
    def insertAtMid(self, info, loc):

        temp = Node(info)
        count = 0
        t1 = self.head
        t2 = None

        if loc == 0:
            self.insertAtBegn(info)
            return
        
        if loc > self.countLinkedList():
            print("ERROR: Index Out Of Range")
            return

        while count is not loc-1:
            count += 1
            t1 = t1.next
        t2 = t1.next
        t1.next = temp
        t1.next.next = t2

    def deleteLinkedList(self, value):
        if self.head is None:
            return

        if self.head.info == value:
            self.head = self.head.next
            return

        t1 = self.head
        prev = None

        while t1 and t1.info != value:
            prev = t1
            t1 = t1.next

        if t1 is None:
            print("Value not found")
            return

        prev.next = t1.next

        
    def printLinkedList(self):

        t1 = self.head

        while t1 is not None:
            print(t1.info)
            t1 = t1.next

    def countLinkedList(self):

        t1 = self.head
        count = 0
        
        while t1 is not None:
            count += 1
            t1 = t1.next
        
        return count

        

obj = singlyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBegn(5)
obj.insertAtBegn(1)
obj.insertAtMid(25,2)
obj.deleteLinkedList(1)
# obj.countLinkedList()
obj.printLinkedList()
