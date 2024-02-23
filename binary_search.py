class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    #creates a string representation of the key values
    def __str__(self):
        return str(self.key)


class BinarySearchTree:
    #establishes the starting point
    def __init__(self):
        self.root = None

    # places nodes into the tree
    def insert(self,key):
        self.root = self._insert(self.root, key)

    # Recursive to include all nodes
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    # searches for the node in a given tree
    def search(self, key):
        return self._search(self.root, key)

    # Recursive to find the node in the tree
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)
        return node
    
    # Finds the minimum value of the tree
    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

# define the data set and fuction
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)
print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
