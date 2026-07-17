class Node:

    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def insertAtBegn(self, value):
        temp = Node(value)

        temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, loc):
        temp = Node(value)
        t1 = self.head

        while(t1.next != None):
            if( t1.info == loc ):
                temp.next = t1.next
                t1.next = temp        
                
            t1 = t1.next

    def insertAtEnd(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t1 = self.head

        while t1.next is not None:
            t1 = t1.next

        t1.next = temp

    def deleteElement(self, value):
        
        t1 = self.head
        prev = t1

        if (t1.info == value ):
            self.head = t1.next
        
        
        
        while t1.next != None:

            
            if (t1.info == value):
                prev.next = t1.next
                break

            
            else: 
                prev = t1
                t1 = t1.next

        if (t1.next == None):
            prev.next = None

    def printLinkedList(self):
        t1 = self.head

        while t1 is not None:
            print(t1.info)
            t1 = t1.next

    


obj = SinglyLinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)

obj.insertAtBegn(21)

obj.insertAtMid(211, 2) # 211 after 20(not index element)

obj.deleteElement(30)

obj.printLinkedList()