class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        # If the tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node

            # Return True to indicate that the node was inserted successfully
            return True

        temp = self.root
        while (True):

            # If the value already exists in the tree, return False
            # to indicate that the insertion was unsuccessful
            if new_node.value == temp.value:
                return False

            # If the value to be inserted < than the current node value
            # go left in the tree and check if the left node is empty
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            # If the value to be inserted > than the current node value
            # go right in the tree and check if the right node is empty
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # Returns True if the value exists in the tree, otherwise False
    # Time complexity: O(log n)
    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))
