# Class representing a BST (Binary Search Tree)
#
# Author: Ben Zwolenik
# Version: 1.0
# Date Created: 5/8/2024 @ 8:24 CST
#
# Operations: add(), remove(), get()


import math
from manim import *

from BSTNode import BSTNode

from ConstructBST import *

class BST:
    # Node properties
    DEPTH = 2
    CHILDREN_PER_VERTEX = 2
    LAYOUT_CONFIG = {"vertex_spacing": (0.0001, .5)}
    VERTEX_CONF = {"radius": 0.35, "color": WHITE}

    # BST representation as a graph
    nodes = set()
    edges = set()

    # Start with empty BST node
    root = None
    scene = None
    height = -1
    
    
    # Initial empty Graph object
    g = None
    c = Circle(radius = .35)

    def __init__(self, scene):
        self.scene = scene
        self.height = -1

    # Adds value to a BST 
    # Time Complexity: Average: O(logn) Worst: O(n)
    # Author: Ben Zwolenik 
    # Version: 1.0 
    # Date Created: 5/8/2024 @ 10:20 CST 
    # Params: self (the current BST object), val (the integer value of the new node), parent (the parent node to create edge) NOT NEEDED IN ACTUAL IMPLEMENTATION
    def add(self, val):
        if (val == None):  
            return
        currHeight = self.height

        self.root = self._addHelper(self.root, val, None, None, '', self.height)

        if (currHeight < self.height and self.height > 1):
            shift = 2 ** (currHeight - 1)
            self.shiftTree(self.root.left, shift, 'L')
            self.shiftTree(self.root.right, shift, 'R')
            if (self.height % 4 == 0):
                self.scene.play(self.scene.camera.frame.animate.scale(1.25))


    def _addHelper(self, curr, val, parent, text, direction, depth):
        if (curr == None):
            newNode = BSTNode(val)
            factor = 0
            if (depth <= 0):
                factor = 1
            else:
                factor = 2 ** depth
            animateAdd(self.scene, self, newNode, parent, self.edges, self.nodes, self.VERTEX_CONF, self.LAYOUT_CONFIG, self.c, text, direction, factor)
            if (depth < 0):
                self.height += 1     
            return newNode
        elif (curr.val < val):
            animateTraverse(self.scene, self, curr, self.c, text)
            curr.right = self._addHelper(curr.right, val, curr, text, 'R', depth - 1)
        elif (curr.val > val):
            animateTraverse(self.scene, self, curr, self.c, text)
            curr.left = self._addHelper(curr.left, val, curr, text, 'L', depth - 1)                                  

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
        
    def getHeight(self, root):
        if (root == None):
            return -1;
        leftHeight = self.getHeight(self, root.left)
        rightHeight = self.getHeight(self, root.right)

        return max(leftHeight, rightHeight) + 1
    
    def shiftTree(self, curr, shift, direction):
        if (curr == None):
            return
        if (shift < 0):
            shift = 1

        shiftTreeAnimate(self.scene, self, curr, shift, direction)
        newShift = math.floor(shift / 2)

        if (direction == 'L'):
            self.shiftTree(curr.left, shift + newShift, 'L')
            self.shiftTree(curr.right, shift - newShift, 'L')
        elif (direction == 'R'):
            self.shiftTree(curr.left, shift - newShift, 'R')
            self.shiftTree(curr.right, shift + newShift, 'R')
        