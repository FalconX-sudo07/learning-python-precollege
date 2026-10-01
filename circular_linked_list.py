# ============================================
# NODE CLASS
# ============================================

class Node:
    # Constructor
    def __init__(self):
        self.data = None
        self.next = None

    # Method for setting the data field
    def setData(self, data):
        self.data = data

    # Method for getting the data field
    def getData(self):
        return self.data

    # Method for setting the next field
    def setNext(self, next):
        self.next = next

    # Method for getting the next field
    def getNext(self):
        return self.next

    # Returns True if node points to another node
    def hasNext(self):
        return self.next != None


# ============================================
# CIRCULAR LINKED LIST CLASS
# ============================================

class CLLList:

    # Constructor
    def __init__(self):
        self.head = None


    # ----------------------------------------
    # COUNT NUMBER OF NODES
    # ----------------------------------------

    def circularListLength(self):

        currentNode = self.head

        if currentNode == None:
            return 0

        count = 1

        while currentNode.next != self.head:
            currentNode = currentNode.next
            count += 1

        return count


    # ----------------------------------------
    # PRINTING THE CONTENTS OF CIRCULAR LIST
    # ----------------------------------------

    def printCircularList(self):

        if self.head == None:
            print("List Empty")
            return

        currentNode = self.head

        print(currentNode.data, end=" ")

        while currentNode.next != self.head:
            currentNode = currentNode.next
            print(currentNode.data, end=" ")

        print()


    # ----------------------------------------
    # INSERTING A NODE AT THE END
    # ----------------------------------------

    def insertAtEndInCLL(self, data):

        newNode = Node()
        newNode.setData(data)

        # Empty list
        if self.head == None:
            self.head = newNode
            newNode.next = newNode
            return

        current = self.head

        # Find the last node
        while current.next != self.head:
            current = current.next

        # New node points to head
        newNode.next = self.head

        # Last node points to new node
        current.next = newNode


    # ----------------------------------------
    # INSERTING A NODE AT THE FRONT
    # ----------------------------------------

    def insertAtBeginningInCLL(self, data):

        current = self.head

        newNode = Node()
        newNode.setData(data)

        # New node initially points to itself
        newNode.next = newNode

        # Empty list
        if self.head == None:
            self.head = newNode

        else:
            # Find the last node
            current = self.head

            while current.next != self.head:
                current = current.next

            # New node points to old head
            newNode.next = self.head

            # Last node points to new node
            current.next = newNode

            # Make new node the head
            self.head = newNode


    # ----------------------------------------
    # DELETE THE LAST NODE
    # ----------------------------------------

    def deleteLastNodeInCLL(self):

        temp = self.head
        current = self.head

        # Empty list
        if self.head == None:
            print("List Empty")
            return

        # Find the last node
        # temp will become the previous node
        while current.next != self.head:
            temp = current
            current = current.next

        # temp is now the node before the last node
        # Make it point to head
        temp.next = self.head

        # If there was only one node
        if current == self.head:
            self.head = None

        return


    # ----------------------------------------
    # DELETE THE FIRST NODE
    # ----------------------------------------

    def deleteFirstNodeInCLL(self):

        current = self.head

        # Empty list
        if self.head == None:
            print("List Empty")
            return

        # Find the last node
        while current.next != self.head:
            current = current.next

        # If there is only one node
        if current == self.head:
            self.head = None
            return

        # Last node points to the second node
        current.next = self.head.next

        # Move head to the second node
        self.head = self.head.next

        return
    
    # ============================================
# EXECUTION / EXAMPLE
# ============================================

cll = CLLList()


# --------------------------------------------
# 1. INSERT ELEMENTS AT END
# --------------------------------------------

cll.insertAtEndInCLL(4)
cll.insertAtEndInCLL(15)
cll.insertAtEndInCLL(7)
cll.insertAtEndInCLL(40)

print("Circular Linked List:")
cll.printCircularList()

print("Number of nodes:", cll.circularListLength())


# --------------------------------------------
# 2. INSERT AT BEGINNING
# --------------------------------------------

cll.insertAtBeginningInCLL(60)

print("\nAfter inserting 60 at beginning:")
cll.printCircularList()

print("Number of nodes:", cll.circularListLength())


# --------------------------------------------
# 3. INSERT ANOTHER NODE AT END
# --------------------------------------------

cll.insertAtEndInCLL(100)

print("\nAfter inserting 100 at end:")
cll.printCircularList()


# --------------------------------------------
# 4. DELETE FIRST NODE
# --------------------------------------------

cll.deleteFirstNodeInCLL()

print("\nAfter deleting first node:")
cll.printCircularList()


# --------------------------------------------
# 5. DELETE LAST NODE
# --------------------------------------------

cll.deleteLastNodeInCLL()

print("\nAfter deleting last node:")
cll.printCircularList()


# --------------------------------------------
# 6. FINAL LENGTH
# --------------------------------------------

print("Final number of nodes:", cll.circularListLength())