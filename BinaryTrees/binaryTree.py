class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Function to print preorder traversal DFS
def printPreorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)

    # Recur on right subtree
    printPreorder(node.right)

# Function to print inorder traversal DFS
def printInorder(node):
    if node is None:
        return

    # First recur on left subtree
    printInorder(node.left)

    # Now deal with the node
    print(node.data, end=' ')

    # Then recur on right subtree
    printInorder(node.right)


# Function to print postorder traversal DFS
def print_postorder(node):
    if node is None:
        return

    # First recur on left subtree
    print_postorder(node.left)

    # Then recur on right subtree
    print_postorder(node.right)

    # Now deal with the node
    print(node.data, end=' ')


# help function for BFS
def level_order_rec(root, level, res):
    # Base case: If node is null, return
    if root is None:
        return

    # Add a new level to the result if needed
    if len(res) <= level:
        res.append([])

    # Add current node's data to its corresponding level
    res[level].append(root.data)

    # Recur for left and right children
    level_order_rec(root.left, level + 1, res)
    level_order_rec(root.right, level + 1, res)

# Function to perform level order traversal
def level_order(root):
    # Stores the result level by level
    res = []
    level_order_rec(root, 0, res)
    return res


# Function to traverse the tree in preorder and check if the given node exists in it
def ifNodeExists(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    # then recur on left subtree
    res1 = ifNodeExists(root.left, key)

    # node found, no need to look further
    if res1:
        return True

    # node is not found in left,
    # so recur on right subtree
    res2 = ifNodeExists(root.right, key)

    return res2



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print('Preorder')
    printPreorder(root)
    print('\n')
    print('printInorder')
    printInorder(root)
    print('\n')
    print('print_postorder')
    print_postorder(root)
    root1 = Node(5)
    root1.left = Node(12)
    root1.right = Node(13)

    root1.left.left = Node(7)
    root1.left.right = Node(14)

    root1.right.right = Node(2)

    root1.left.left.left = Node(17)
    root1.left.left.right = Node(23)

    root1.left.right.left = Node(27)
    root1.left.right.right = Node(3)

    root1.right.right.left = Node(8)
    root1.right.right.right = Node(11)
    print('\n')
    res = level_order(root1)
    for level in res:
        print(f'[{', '.join(map(str, level))}] ', end='')
    print('\n')


    print('Node 5 exists in tree:', ifNodeExists(root1, 5))
    print('Node 17 exists in tree:', ifNodeExists(root1, 17))
    print('Node 55 exists in tree:', ifNodeExists(root1, 55))