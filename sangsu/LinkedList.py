class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, data):
        if not self.head:
            self.head = Node(data)
            
        else:
            current = self.head
            while current.next:
                current = current.next
                
            current.next = Node(data)
    
    
            
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    
linkedList = LinkedList()
linkedList.insertNode(3)
linkedList.insertNode(4)
linkedList.insertNode(5)
linkedList.printList()
