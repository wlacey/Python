class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value> temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    # Takes in current node as a starting point.
    def min_value_node(self, current_node):
        # Will traverse tree until it hits the last node.
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

# Driver Code
tree = BST()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)
print(tree.min_value_node(tree.root))
print(tree.min_value_node(tree.root.right))
