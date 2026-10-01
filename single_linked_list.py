class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next !=None
    
class SLList(object):
    def __init__(self,node = None):
        self.length = 0
        self.head = node
    
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.next
        return count
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.data = data
        
        if self.length ==0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length+=1
    def insertAtEnd(self,data):
        newNode = Node()
        newNode.data = data
        current = self.head
        while current.next !=None:
            current = current.next
        current.next = newNode
        self.length+=1
    def insertAtGivenPosition(self,pos,data):
        if pos > self.length or pos < 0 :
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    count = 1
                    current = self.head
                    while count<pos-1:
                        count+=1
                        current = current.next
                    newNode.next = current.next     #erases the previous link of current to next
                    current.next = newNode
                    self.length+=1
    def deleteFromBeginning(self):
        if self.length ==0 :
            print("Empty List!")
            
        else:
            self.head = self.head.next
            self.length-=1
    def deleteFromEnd(self):
        if self.length==0:
            print("List is Empty!")
        else:
            currentnode = self.head
            previousnode = self.head
            while currentnode.next != None:
                previousnode=currentnode
                currentnode=currentnode.next
                previousnode.next=None
                self.length-=1
    #def deleteWithNode(self):
    
    
    