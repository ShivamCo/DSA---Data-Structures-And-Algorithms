

class Node:
    def __init__(self, info, prev=None, next=None):

        self.info = info
        self.prev = prev
        self.next = next

class DLinkedList:

    def __init__(self, head=None):
        self.head = head

    def insertAtBegn(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return


        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        


    def insertAtMid(self, value, loc):
        count = 0
        Dlist_Count = self.countDLinkedList()

        if loc > Dlist_Count:
            print(" \n ERROR: Can't Insert Value, Out of Range! \n")
            return

        if loc == 0:
            self.insertAtBegn(value)
            return

        if loc == Dlist_Count:
            self.insertAtEnd(value)
            return

        t1 = self.head

        while count != loc - 1:
            count += 1
            t1 = t1.next

        temp_next = t1.next
        new_node = Node(value, t1, temp_next)  
        t1.next = new_node

        if temp_next is not None:
            temp_next.prev = new_node           

        
        
    def insertAtEnd(self, value):
        temp = Node(value)
        
        if self.head is None:
            self.head = temp
            return
        
        t1 = self.head
        t2 = t1

        while t1.next is not None:
            t2 = t1
            t1 = t1.next 

        t1.next = Node(value,t1)
    
    def printDLinkedList(self):

        t1 = self.head
        
        count = 0
    

        while t1 is not None:

            node_values = Node(t1.info, t1.prev, t1.next)
            

            print(f"Value: {node_values.info}, Prev: {node_values.prev}, Next: {node_values.next}")
           
            t1 = t1.next
            count += 1

        return count

    def countDLinkedList(self):
        t1 = self.head
        count = 0
        
        while t1 is not None:
            t1 = t1.next
            count += 1

        return count
    
    def deleteItem(self, value):
    
        t1 = self.head

        if t1 is None:
            return

        if t1.info == value:
            self.head = t1.next
            if self.head is not None:
                self.head.prev = None
            return
    
        while t1.next is not None and t1.next.info != value:
            t1 = t1.next
    
        if t1.next is None:
            print(f"Value {value} not found in list.")
            return

        t1.next = t1.next.next
        if t1.next is not None:
            t1.next.prev = t1

        
    
    

obj = DLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)

obj.insertAtBegn(5)
obj.insertAtBegn(1)


obj.insertAtMid(111,6)
obj.insertAtMid(222,2)

obj.deleteItem(1)
obj.deleteItem(30)


obj.printDLinkedList()
