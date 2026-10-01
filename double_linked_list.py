class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next != None
    def setPrev(self,prev):
        self.prev = prev
    def getPrev(self):
        return self.prev
    def hasPrev(self):
        return self.prev != None
    #returns string equivalent of object
    def __str__(self):
        return "Node[Data = %s]%(self.data,)"


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtBeginning(self,data):
        newNode = Node(data,None,None)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def insertAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            newNode = Node(data)
            newNode.prev = current
            newNode.next = None
                  