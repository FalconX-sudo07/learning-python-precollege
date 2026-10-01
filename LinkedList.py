# ============================================
# LINKED LISTS IN PYTHON - BEGINNER GUIDE
# ============================================

# A linked list is made up of NODES.
#
# Each node contains:
#   1. data -> the value stored in the node
#   2. next -> a reference to the next node
#
# Example:
#
# [10 | next] -> [20 | next] -> [30 | None]
#
# The first node is called the HEAD.
# None means there is no next node.


# ============================================
# 1. CREATING A NODE
# ============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a node
a = Node(10)

print("First node:")
print(a.data)       # 10
print(a.next)       # None


# ============================================
# 2. CONNECTING NODES
# ============================================

a = Node(10)
b = Node(20)
c = Node(30)

# Connect the nodes
a.next = b
b.next = c

# We now have:
#
# a
# ↓
# [10] -> [20] -> [30] -> None
#          ↑       ↑
#          b       c


# ============================================
# 3. HEAD
# ============================================

# The head is the first node of the linked list.

head = a

print("\nHead:")
print(head.data)    # 10

# The list is:
#
# head
#  ↓
# [10] -> [20] -> [30] -> None


# ============================================
# 4. TRAVERSING A LINKED LIST
# ============================================

print("\nTraversing the linked list:")

current = head

while current != None:
    print(current.data)
    current = current.next

# Output:
# 10
# 20
# 30


# ============================================
# 5. INSERT AT THE BEGINNING
# ============================================

def insert_at_beginning(head, data):

    # Create a new node
    new_node = Node(data)

    # Make the new node point to the old head
    new_node.next = head

    # Make the new node the new head
    head = new_node

    return head


# Current list:
#
# 10 -> 20 -> 30 -> None

head = insert_at_beginning(head, 5)

# New list:
#
# 5 -> 10 -> 20 -> 30 -> None

print("\nAfter inserting 5 at beginning:")

current = head

while current != None:
    print(current.data)
    current = current.next


# ============================================
# 6. INSERT AT THE END
# ============================================

def insert_at_end(head, data):

    # Create a new node
    new_node = Node(data) 

    # If the list is empty,
    # the new node becomes the head
    if head == None:
        return new_node

    # Start at the head
    current = head

    # Move until we reach the last node
    while current.next != None:
        current = current.next

    # Connect the last node to the new node
    current.next = new_node

    return head


# Current:
#
# 5 -> 10 -> 20 -> 30 -> None

head = insert_at_end(head, 40)

# Now:
#
# 5 -> 10 -> 20 -> 30 -> 40 -> None

print("\nAfter inserting 40 at end:")

current = head

while current != None:
    print(current.data)
    current = current.next


# ============================================
# 7. SEARCHING FOR A VALUE
# ============================================

def search(head, target):

    current = head

    while current != None:

        if current.data == target:
            return True

        current = current.next

    return False


print("\nSearching:")

print(search(head, 20))   # True
print(search(head, 99))   # False


# ============================================
# 8. DELETE A NODE
# ============================================

def delete_node(head, value):

    # If the list is empty
    if head == None:
        return None

    # If the node we want to delete
    # is the first node
    if head.data == value:
        return head.next

    current = head

    # Find the node BEFORE the one
    # we want to delete
    while current.next != None:

        if current.next.data == value:

            # Skip over the node
            current.next = current.next.next

            return head

        current = current.next

    return head


# Current:
#
# 5 -> 10 -> 20 -> 30 -> 40 -> None

head = delete_node(head, 30)

# Now:
#
# 5 -> 10 -> 20 -> 40 -> None

print("\nAfter deleting 30:")

current = head

while current != None:
    print(current.data)
    current = current.next


# ============================================
# 9. PROPER LINKED LIST CLASS
# ============================================

# Instead of manually managing the head,
# we can create a LinkedList class.


class LinkedList:

    def __init__(self):
        self.head = None

    # ----------------------------------------
    # ADD TO END
    # ----------------------------------------

    def append(self, data):

        new_node = Node(data)

        # If list is empty
        if self.head == None:
            self.head = new_node
            return

        # Find the last node
        current = self.head

        while current.next != None:
            current = current.next

        # Connect last node to new node
        current.next = new_node

    # ----------------------------------------
    # ADD TO BEGINNING
    # ----------------------------------------

    def prepend(self, data):

        new_node = Node(data)

        # New node points to current head
        new_node.next = self.head

        # New node becomes the head
        self.head = new_node

    # ----------------------------------------
    # DISPLAY
    # ----------------------------------------

    def display(self):

        current = self.head

        while current != None:
            print(current.data)
            current = current.next

    # ----------------------------------------
    # SEARCH
    # ----------------------------------------

    def search(self, target):

        current = self.head

        while current != None:

            if current.data == target:
                return True

            current = current.next

        return False

    # ----------------------------------------
    # DELETE
    # ----------------------------------------

    def delete(self, value):

        # Empty list
        if self.head == None:
            return

        # Delete the head
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next != None:

            if current.next.data == value:

                current.next = current.next.next
                return

            current = current.next


# ============================================
# 10. USING THE LINKED LIST CLASS
# ============================================

numbers = LinkedList()

numbers.append(10)
numbers.append(20)
numbers.append(30)

print("\nLinkedList class:")
numbers.display()

# Output:
# 10
# 20
# 30


# ============================================
# 11. PREPEND
# ============================================

numbers.prepend(5)

print("\nAfter prepend(5):")
numbers.display()

# 5
# 10
# 20
# 30


# ============================================
# 12. SEARCH
# ============================================

print("\nSearching in LinkedList:")

print(numbers.search(20))   # True
print(numbers.search(100))  # False


# ============================================
# 13. DELETE
# ============================================

numbers.delete(20)

print("\nAfter deleting 20:")
numbers.display()

# 5
# 10
# 30


# ============================================
# FINAL STRUCTURE
# ============================================

# After all the operations, our list looks like:
#
# numbers
#    |
#   head
#    ↓
# [5] -> [10] -> [30] -> None
#
#
# Each node contains:
#
# [data | next]
#
# data = the value
# next = reference to the next node
#
#
# The most important operations are:
#
# append()       -> add at the end
# prepend()      -> add at the beginning
# search()       -> find a value
# delete()       -> remove a value
# display()      -> traverse the list