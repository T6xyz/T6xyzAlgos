# Class representing a BST Node (Binary Search Tree Node
#
# Author: Ben Zwolenik
# Version: 1.0
# Date Created: 5/8/2024 @ 9:20 CST
#
class BSTNode:
    
    # Since adding to our BST is always at a leaf node, both children will always be null
    # This can be changed when we use add() and utilize pointer reinforcement
    # Author: Ben Zwolenik
    # Version: 1.0
    # Date Created: 5/8/2024 @ 9:20 CST 
    # Params: self (the current object), val (the integer value of the new node)
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None