# Class representing a BST (Binary Search Tree)
#
# Author: Ben Zwolenik
# Version: 1.0
# Date Created: 5/8/2024 @ 8:24 CST
#
# Operations: add(), remove(), get()


from manim import *

from BSTNode import BSTNode

class BST:
    # Node properties
    DEPTH = 2
    CHILDREN_PER_VERTEX = 2
    LAYOUT_CONFIG = {"vertex_spacing": (0.001, 1)}
    VERTEX_CONF = {"radius": 0.35, "color": WHITE}

    # BST representation as a graph
    nodes = {}
    edges = {}
    # Start with empty BST node
    root = BSTNode(None)
    
    # Initial empty Graph object
    g = None
    c = Circle(radius=.35)


    # Empty contructor (FIX LATER)
    def __init__ (self):
        pass

    # Adds value to a BST 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik
    # Version: 1.0
    # Date Created: 5/8/2024 @ 10:20 CST 
    # Params: self (the current BST object), val (the integer value of the new node)
    def add(self, val):
        if (val == None):
            return
        self._addHelper(self.root, val)

    def _addHelper(curr, val):
        if (curr == None):
            newNode = BSTNode(val)
            return newNode
        if (curr.val < val):
            curr.right = curr._addHelper(curr.right, val)
        elif (curr.val > val):
            curr.left = curr._addHelper(curr.left, val)
        return curr
            
    # Removes a value to a BST 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik
    # Version: 1.0
    # Date Created: 5/8/2024 @ 10:26 CST 
    # Params: self (the current BST object), val (the integer value of node to be removed)
    def remove(self, val):
        if (val == None):
            return
        self._helperRemove(self.root, val)
    
    def _helperRemove(curr, val):
        if (curr == None):
            raise Exception("Val could not be found in BST!")
        if (curr.val < val):
            curr.right = curr._helperRemove(curr.right, val)
        elif (curr.val > val):
            curr.left = curr._helperRemove(curr.left, val)
        elif (curr.val == val):
            if (curr.left == None and curr.right == None):
                return None
            if (curr.left == None and curr.right != None):
                return curr.right
            if (curr.left != None and curr.right == None):
                return curr.left
            
            dummy = BSTNode()
            curr.right = curr._findSuccessor(curr.right, dummy)
            curr.val = dummy.val
        return curr
    
    # Finds the successor node of a given node 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik
    # Version: 1.0
    # Date Created: 5/8/2024 @ 10:25 CST 
    # Params: self (the current BST node), dummy (a node to hold the value of the successor node)
    def _findSuccessor(curr, dummy):
        if (curr.left == None):
            dummy.val = curr.val
            return curr.right
        curr.left = curr._findSuccessor(curr.left, dummy)
        return curr
    
    # Gets a value from a BST 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik
    # Version: 1.0
    # Date Created: 5/8/2024 @ 10:31 CST 
    # Params: self (the current BST object), val (the integer value to search for in the BST)
    def get(self, val):
        if (self.root == None or val == None):
            return False
        return self._getHelper(self.root, val)
        
    def _getHelper(self, curr, val):
        if (curr == None):
            return False
        if (curr.val > val):
            return self._getHelper(curr.left, val)
        elif (curr.val < val):
            return self._getHelper(curr.right, val)
        else:
            return True