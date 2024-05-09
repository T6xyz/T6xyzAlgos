# Class representing a BST (Binary Search Tree)
#
# Author: Ben Zwolenik
# Version: 1.0
# Date Created: 5/8/2024 @ 8:24 CST
#
# Operations: add(), remove(), get()


from manim import *

from BSTNode import BSTNode

from ConstructBST import *

class BST:
    # Node properties
    DEPTH = 2
    CHILDREN_PER_VERTEX = 2
    LAYOUT_CONFIG = {"vertex_spacing": (0.001, 1)}
    VERTEX_CONF = {"radius": 0.35, "color": WHITE}

    # BST representation as a graph
    nodes = set()
    edges = set()

    # Start with empty BST node
    root = BSTNode(None)
    scene = None
    
    
    # Initial empty Graph object
    g = None
    c = Circle(radius = .35)

    def __init__(self, scene):
        self.scene = scene

    # Adds value to a BST 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik 
    # Version: 1.0
    # Date Created: 5/8/2024 @ 10:20 CST 
    # Params: self (the current BST object), val (the integer value of the new node), parent (the parent node to create edge) NOT NEEDED IN ACTUAL IMPLEMENTATION
    def add(self, val):
        if (val == None):
            return
        self._addHelper(self.root, val, None, None)

    def _addHelper(self, curr, val, parent, text):
        if (curr == None):
            newNode = BSTNode(val)
            animateAdd(self.scene, self, newNode, parent, self.edges, self.nodes, self.VERTEX_CONF, self.LAYOUT_CONFIG, self.c, text)
            return newNode
        if (curr.val < val):
            animateTraverse()
            curr.right = self._addHelper(self, curr.right, val, curr, text)
        elif (curr.val > val):
            animateTraverse()
            curr.left = self._addHelper(self, curr.left, val, curr, text)
        return curr
            
    # Removes a value to a BST 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik
    # Version: 1.0
    # Date Created: 5/8/2024 @ 10:26 CST 
    # Params: self (the current BST object), val (the integer value of node to be removed), parent (the parent node to create edge) NOT NEEDED IN ACTUAL IMPLEMENTATION
    def remove(self, val):
        if (val == None):
            return
        self._helperRemove(self.root, val, None)
    
    def _helperRemove(curr, val, parent):
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
            curr.right = curr._findSuccessor(curr.right, dummy, curr.right)
            curr.val = dummy.val
        return curr
    
    # Finds the successor node of a given node 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik
    # Version: 1.0
    # Date Created: 5/8/2024 @ 10:25 CST 
    # Params: self (the current BST node), dummy (a node to hold the value of the successor node), parent (the parent node to create edge) NOT NEEDED IN ACTUAL IMPLEMENTATION
    def _findSuccessor(curr, dummy, parent):
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
    # Params: self (the current BST object), val (the integer value to search for in the BST), parent (the parent node to create edge) NOT NEEDED IN ACTUAL IMPLEMENTATION
    def get(self, val):
        if (self.root == None or val == None):
            return False
        return self._getHelper(self.root, val, None)
        
    def _getHelper(self, curr, val, parent):
        if (curr == None):
            return False
        if (curr.val > val):
            return self._getHelper(curr.left, val)
        elif (curr.val < val):
            return self._getHelper(curr.right, val)
        else:
            return True