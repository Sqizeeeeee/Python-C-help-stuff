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

# Find size of linked list
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

# insert at front
def insert_at_front(head, new_data):
    
    # Create a new node
    new_node = Node(new_data)

    # Make next of new node as head
    new_node.next = head

    # Change prev of head node to new node
    if head is not None:
        head.prev = new_node

    # Return the new node as the head of the doubly linked list
    return new_node

# insert at any position
def insert_at_position(head, pos, new_data):
  
    # Create a new node
    new_node = Node(new_data)

    # Insertion at the beginning
    if pos == 1:
        new_node.next = head

        # If the linked list is not empty, set the prev of head to new node
        if head is not None:
            head.prev = new_node

        # Set the new node as the head of the linked list
        head = new_node
        return head

    curr = head
    
    # Traverse the list to find the node before the insertion point
    for _ in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next

    # If the position is out of bounds
    if curr is None:
        print("Position is out of bounds.")
        return head

    # Set the prev of new node to curr
    new_node.prev = curr

    # Set the next of new node to next of curr
    new_node.next = curr.next

    # Update the next of current node to new node
    curr.next = new_node

    # If the new node is not the last node, update prev of next node to new node
    if new_node.next is not None:
        new_node.next.prev = new_node

    return head

# insert at the end
def insert_end(head, new_data):
  	
    # Create a new node
    new_node = Node(new_data)
    
    # If the linked list is empty, set the new node as the head
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        # Set the next of the last node to the new node
        curr.next = new_node
        
        # Set the prev of the new node to the last node
        new_node.prev = curr
    
    return head

# Function to delete the first node (head) of the list
# and return the second node as the new head
def del_head(head):
  
    # If empty, return None
    if head is None:
        return None

    # Store in temp for deletion later
    temp = head

    # Move head to the next node
    head = head.next

    # Set prev of the new head
    if head is not None:
        head.prev = None

    # Return new head
    return head

# Function to delete a node at a specific position 
# in the doubly linked list
def del_pos(head, pos):

    # If the list is empty
    if head is None:
        return head

    curr = head

    for i in range(1, pos):
        if curr is None:
            break
        curr = curr.next

    if curr is None:
        return head

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = curr.next

    # Update the next node's prev pointer
    if curr.next is not None:
        curr.next.prev = curr.prev

    # If the node to be deleted is the head node
    if head == curr:
        head = curr.next

    # Deallocate memory for the deleted node
    del curr
    return head

# Delete last node
def del_last(head):
  
    # Corner cases
    if head is None:
        return None
    if head.next is None:
        return None

    # Traverse to the last node
    curr = head
    while curr.next is not None:
        curr = curr.next

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = None

    # Return the updated head
    return head



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

def insertFrontUsage():
    # Create a hardcoded doubly linked list:
    # 2 <-> 3 <-> 4 -> NULL
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end='')
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Node at the front:", end='')
    data = 1
    head = insert_at_front(head, data)

    # Print the updated list
    print_list(head)

def insert_at_positionUsage():
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List: ", end="")
    print_list(head)

    # Insert new node with data 3 at position 3
    print("Inserting Node with data 3 at position 3: ", end="")
    data = 3
    pos = 3
    head = insert_at_position(head, pos, data)

    # Print the updated list
    print_list(head)

def insert_at_the_endUsage():
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List: ", end="")
    print_list(head)

    # Insert a new node with data 4 at the end
    print("Inserting Node with data 4 at the end: ", end="")
    data = 4
    head = insert_end(head, data)

    # Print the updated list
    print_list(head)


def del_headUsage():
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    print("Original Linked List: ", end="")
    print_list(head)

    print("After Deletion at the beginning: ", end="")
    head = del_head(head)

    print_list(head)

def del_posUsage():
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    print('before:', print_list(head))
    head = del_pos(head, 2)
    print('after')
    print_list(head)

def del_lastUsage():
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    print("Original Linked List: ", end="")
    print_list(head)

    print("After Deletion at the end: ", end="")
    head = del_last(head)

    print_list(head)



def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end='')
        curr = curr.next
    print()


def main():
    print('traversal--------------------------------------------------------------------')
    traversalUsage()
    print('size---------------------------------------------------------------------')
    findSizeUsage()
    print('insertion-------------------------------------------------------------------------')
    insertFrontUsage()
    insert_at_positionUsage()
    insert_at_the_endUsage()
    print('deletion------------------------------------------------------------------------')
    del_headUsage()
    del_posUsage()
    del_lastUsage()




if __name__ == '__main__':
    main()