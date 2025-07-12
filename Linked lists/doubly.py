class Node:
  
    def __init__(self, data):
        # To store the value or data.
        self.data = data

        # Reference to the previous node
        self.prev = None

        # Reference to the next node
        self.next = None



# Function to traverse the doubly linked list
# in forward direction        
def forward_traversal(head):
    curr = head
    while curr is not None:
        
        # Output data of the current node
        print(curr.data, end=" ")
        
        # Move to the next node
        curr = curr.next
    
    print()

def forward_traversalRec(head):
    if head is None:
        return
    
    # Print current node's data
    print(head.data, end=" ")
    
    # Recursive call with the next node
    forward_traversalRec(head.next)

def findSize(curr):
    size = 0
    while curr:
        size += 1
        curr = curr.next
    return size

def findSizeRec(head):
    if head is None:
        return 0
    return 1 + findSize(head.next)  # Recursive cal



def traversalUsage():
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal: ", end="")
    forward_traversal(head)
    forward_traversalRec(head)

def findSizeUsage():
    # Create a hard-coded doubly linked list:
    # 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print(findSize(head))
    print(findSizeRec(head))


def main():
    traversalUsage()
    findSizeUsage()


if __name__ == '__main__':
    main()