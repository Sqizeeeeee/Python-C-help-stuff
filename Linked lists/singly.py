# A linked list node
class Node:
    # Constructor to initialize a new node with data
    def __init__(self, data):
       # Data part of the node
        self.data = data   
        self.next = None



# Function to traverse and print the singly linked list Itaretive variation
def traverseListItaretive(head):

    # A loop that runs till head is nullptr
    while head is not None:

		# Printing data of current node
        print(head.data, end=" ")
        
		# Moving to the next node
        head = head.next
    print()

# Function to traverse and print the singly linked list recursive variation
def traverseListRecursive(head):

  
    # Base condition is when the head is nullptr
    if head is None:
        print()
        return
      
    # Printing the current node data
    print(head.data, end=" ")
    
    # Moving to the next node
    traverseListRecursive(head.next)

# Checks whether key is present in linked list Itaretive variation
def searchItaretive(head, key:int) -> bool:
    # Initialize curr with the head of linked list
    curr = head

    # Iterate over all nodes
    while curr is not None:

        # If the current node's value is equal to key,
        # return true
        if curr.data == key:
            return True
        
        # Move to next node
        curr = curr.next

    # Return False if there's no node with key
    return False

# Checks whether key is present in linked list recursive variation
def searchRecursive(head, key:int) -> bool:
    # Base case
    if head is None:
        return False
    
    # If key is present in current node, return true
    if head.data == key:
        return True
    # Recur for remaining list
    return searchRecursive(head.next, key)

# Counts length iterative variation
def lengthIterative(head) -> int:
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count

# Counts length recursive variation
def lengthRecursive(head) -> int:

    if head is None:
        return 0
    
    return 1 + lengthRecursive(head.next)

# Insert a node in the front
def insertFront(head, new):
    # Create a new node with the given data
    new_node = Node(new)

    # Make the next of the new node point to the current head
    new_node.next = head

    # Return the new node as the new head of the list
    return new_node

# Insert a node at any position
def insertMiddle(head, pos:int, new: int):
    # This condition to check whether the
    # position given is valid or not.
    if pos < 1:
        return head
    
    # head will change if pos=1
    if pos == 1:
        new_node = Node(new)
        new_node.next = head
        return new_node
    
    curr = head
    
    # Traverse to the node that will be 
    # present just before the new node
    for _ in range(1, pos - 1):
        if curr == None:
            break
        curr = curr.next
        
    # if position is greater
    # number of nodes
    if curr is None:
        return head
    
    new_node = Node(new)
    
    # update the next pointers
    new_node.next = curr.next
    curr.next = new_node
    
    return head

# Insert a node at the end
def insertEnd(head, new):
    # Create new node
    new_node = Node(new)

    # If the Linked List is empty, make the 
    # new node as the head and return
    if head is None:
        return new_node
    
    # Store the head reference in a temporary variable
    last = head

    # Traverse till the last node
    while last.next:
        last = last.next

    # Change the next pointer of the last 
    # node to point to the new node
    last.next = new_node

    # Return the head of the list
    return head

# Delete front Node
def deleteFront(head):

    # Check if the list is empty
    if head is None:
        return None

    # Store the current head in a temporary variable
    temp = head

    # Move the head pointer to the next node
    head = head.next

    # Delete the old head by removing the reference
    del temp

    return head

# Delete middle node
def deleteMiddle(head, pos:int):
    temp = head
    prev = None

    # Base case if linked list is empty
    if temp is None:
        return head

    # Case 1: Head is to be deleted
    if pos == 1:
        head = temp.next
        return head

    # Case 2: Node to be deleted is in middle
    # Traverse till given position
    for i in range(1, pos):
        prev = temp
        temp = temp.next
        if temp is None:
            print("Data not present")
            return head

    # If given position is found, delete node
    if temp is not None:
        prev.next = temp.next

    return head

# Delete last node
def deleteEnd(head):
    # If the list is empty, return None
    if not head:
        return None

    # If the list has only one node, delete it and return None
    if not head.next:
        return None

    # Find the second last node
    second_last = head
    while second_last.next.next:
        second_last = second_last.next

    # Delete the last node
    second_last.next = None

    return head

# Reverse Linked list
def reverseList(head):

    # Initialize three pointers: curr, prev and next
    curr = head
    prev = None

    # Traverse all the nodes of Linked List
    while curr is not None:

        # Store next
        nextNode = curr.next

        # Reverse current node's next pointer
        curr.next = prev

        # Move pointers one position ahead
        prev = curr
        curr = nextNode

    # Return the head of reversed linked list
    return prev


# Traversal means visiting each Node and performing operations like printing or processing data
def traversalUsage():
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    # Example of traversing the node and printing
    traverseListItaretive(head)
    traverseListRecursive(head)

# Checks whether key is present in linked list
def searchUsage():
    # Create a hard-coded linked list:
    # 14 -> 21 -> 13 -> 30 -> 10
    head = Node(14)
    head.next = Node(21)
    head.next.next = Node(13)
    head.next.next.next = Node(30)
    head.next.next.next.next = Node(10)

    # Key to search in the linked list
    key = 14

    if searchRecursive(head, key):
        print("Yes")
    else:
        print("No")
    
    if searchItaretive(head, key):
        print("Yes")
    else:
        print("No")

# Counts length of Linked list
def lengthUsage():
    # Create a hard-coded linked list:
    # 1 -> 3 -> 1 -> 2 -> 1
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    # Function call to count the number of nodes
    print("Count of nodes is", lengthRecursive(head))
    print("Count of nodes is", lengthIterative(head))

# Insert new node at the beggining of the list
def insertionFrontUsage():
    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # Print the original list
    print("Original Linked List:", end="")
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Nodes at the front:", end="")
    data = 1
    head = insertFront(head, data)

    # Print the updated list
    print_list(head)

# Insert new node at any position
def insertionAnyUsage():
    # Creating the list 3->5->8->10
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(10)
    print('Old list')
    print_list(head)
    data = 12
    pos = 3
    head = insertMiddle(head, pos, data)
    print('New list')
    print_list(head)

# Insert new node at the end of the list
def insertionEndUsage():

    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # Print the original list
    print("Original Linked List:", end="")
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Nodes at the front:", end="")
    data = 6
    head = insertFront(head, data)

    # Print the updated list
    print_list(head)

# Delete front node
def deletionFronUsage():
        # Create a hard-coded linked list:
    # 3 -> 12 -> 15 -> 18
    head = Node(3)
    head.next = Node(12)
    head.next.next = Node(15)
    head.next.next.next = Node(18)
    print('old list')
    print_list(head)
    head = deleteFront(head)
    print('new list')
    print_list(head)

# Delete middle node
def deletionMiddleUsage():
    # Creating a static linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Print original list
    print("Original list: ", end="")
    print_list(head)

    # Deleting node at position 2
    position = 2
    head = deleteMiddle(head, position)

    # Print list after deletion
    print("List after deletion: ", end="")
    print_list(head)

# Delete last node
def deletionEndUsage():
    # Creating a static linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ")
    print_list(head)

    # Removing the last node
    head = deleteEnd(head)

    print("List after removing the last node: ")
    print_list(head)

# Reverse List
def reverseUsage():
    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    print_list(head)

    head = reverseList(head)

    print("Reversed Linked List:", end="")
    print_list(head)



# Print list
def print_list(head):
    # Start from the head of the list
    curr = head

    # Traverse the list
    while curr is not None:
        # Print the current node's data
        print(f" {curr.data}", end="")

        # Move to the next node
        curr = curr.next

    # Print a newline at the end
    print()

def main():
    print('travesral----------------------------------------------------------------------')
    traversalUsage()
    print('search----------------------------------------------------------------------')
    searchUsage()
    print('length----------------------------------------------------------------------')
    lengthUsage()
    print('insertion----------------------------------------------------------------------')
    insertionFrontUsage()
    insertionAnyUsage()
    insertionEndUsage()
    print('deletion--------------------------------------------------------------------')
    deletionFronUsage()
    deletionMiddleUsage()
    deletionEndUsage()
    print('reverse-----------------------------------------------------------------------')
    reverseUsage()






if __name__ == '__main__':
    main()